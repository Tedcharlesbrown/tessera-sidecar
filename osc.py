import argparse
import math
import time
from pythonosc import dispatcher
from pythonosc import osc_server

from api import *
from functions import *
from companion import *

def setupProcessor(unused_addr,processor,ip,maxBright):
    #get total number of processors
    global numProcessors
    if numProcessors <= processor:
        numProcessors = processor + 1
    #assign new arrays
    ip_array.insert(processor,ip_prefix + ip)
    max_brightness_array.insert(processor,maxBright)
    
    #clear all previously used arrays
    if len(ip_array) > numProcessors:
        i = numProcessors
        while i < len(ip_array):
            ip_array.pop(i)
            max_brightness_array.pop(i)

    print(ip_array,max_brightness_array,numProcessors)

# buttonHeld = False

def buttonHold(unused_addr,button):
    global buttonHeld
    buttonHeld = button[0]

def parseBrightnessStep(unused_addr,processor,step):
    while buttonHeld > 0:
        currentBrightness = getBrightness(processor)
        newBrightness = currentBrightness + step
        sendBrightness(unused_addr,processor,newBrightness)
        time.sleep(0.25)

def parseBrightnessPercent(unused_addr,processor,percent):
    percent = normalize(percent,0,100,0,1)
    newBrightness = int(max_brightness_array[0]) * percent
    sendBrightness(unused_addr,processor,int(newBrightness))

def startOSC():
    global dispatcher
    global OSCServer
    global osc_client
    # if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",default="127.0.0.1", help="The ip to listen on")
    parser.add_argument("--port",type=int, default=5005, help="The port to listen on")
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    parseOSC(dispatcher)
    # dispatcher.map("/test", testFunction)

    OSCServer = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatcher)
    print("Serving on {}".format(OSCServer.server_address))
    OSCServer.serve_forever()

def parseOSC(oscMessage):
    dispatcher.map("/setup",setupProcessor)
    dispatcher.map("/setup/feedback",setup_button_text)

    dispatcher.map("/on",buttonHold,1)
    dispatcher.map("/off",buttonHold,0)

    dispatcher.map("/brightness",sendBrightness)
    dispatcher.map("/brightness/step",parseBrightnessStep)
    dispatcher.map("/brightness/percent",parseBrightnessPercent)
    dispatcher.map("/temperature",sendTemperature)

    


# def stopOSC():
#     OSCServer.shutdown()
#     print("server exit")
