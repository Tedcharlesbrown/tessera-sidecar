import argparse
import math
import time
from pythonosc import dispatcher
from pythonosc import osc_server

from globals import *
from api import *
from functions import *
from companion import *

#------------------------------------------------------------------------------
# SETUP
def setup_page_osc(verbose):
    if verbose:
        print("OSC PAGE SETUP")

#------------------------------------------------------------------------------
# UPDATE
def update_page_osc():
    x = 0

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
    newBrightness = int(read(processor_array[processor].get("MAX_BRIGHTNESS"))) * percent
    sendBrightness(unused_addr,processor,int(newBrightness))

def parseTemperatureStep(unused_addr,processor,step):
    while buttonHeld > 0:
        currentTemperature = get_temperature(processor)
        newTemperature = currentTemperature + step
        sendTemperature(unused_addr,processor,newTemperature)
        time.sleep(0.25)

def startOSC():
    global dispatcher
    global OSCServer
    global osc_client
    global osc_server_is_running
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",default="127.0.0.1", help="The ip to listen on")
    parser.add_argument("--port",type=int, default=settings.get("OSC PORT"), help="The port to listen on")
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    parseOSC(dispatcher)
    

    OSCServer = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatcher)
    print("LISTENING TO OSC FROM {}".format(OSCServer.server_address))
    osc_server_is_running = True
    OSCServer.serve_forever()

def parseOSC(oscMessage):
    dispatcher.map("/on",buttonHold,1)
    dispatcher.map("/off",buttonHold,0)

    dispatcher.map("/brightness",sendBrightness)
    dispatcher.map("/brightness/step",parseBrightnessStep)
    dispatcher.map("/brightness/percent",parseBrightnessPercent)
    dispatcher.map("/temperature",sendTemperature)
    dispatcher.map("/temperature/step",parseTemperatureStep)