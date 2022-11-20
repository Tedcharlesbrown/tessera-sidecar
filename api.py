import requests

from globals import *
from osc import *
from companion import *

# TESSERA API VARIABLES
api = {}
api["prefix"] = "/api"
# INPUT
api["refresh_rate"] = [api["prefix"] + "/input/active/refresh-rate"]
api["input_res_height"] = [api["prefix"] + "/input/active/resolution/height"]
api["input_res_width"] = [api["prefix"] + "/input/active/resolution/width"]
api["input_portNumber"] = [api["prefix"] + "/input/active/source/port-number"]
api["input_portType"] = [api["prefix"] + "/input/active/source/port-type"]
# OUTPUT
api["brightness"] = [api["prefix"] + "/output/global-colour/brightness"]
api["temperature"] = [api["prefix"] + "/output/global-colour/colour-temperature"]
api["dark_magic"] = [api["prefix"] + "/output/global-colour/dark-magic/enabled"]

# OVERIDE
api["blackout"] = [api["prefix"] + "/override/blackout/enabled"]
api["blackout_fade"] = [api["prefix"] + "/override/blackout/fade-time"]
api["freeze"] = [api["prefix"] + "/override/freeze/enabled"]
api["test_pattern"] = [api["prefix"] + "/override/test-pattern/enabled"]
api["test_format"] = [api["prefix"] + "/override/test-pattern/format"]
api["test_type"] = [api["prefix"] + "/override/test-pattern/type"]


#------------------------------------------------------------------------------
# SETUP
def setup_page_api(verbose):
    if verbose:
        print("API PAGE SETUP")


#------------------------------------------------------------------------------
# UPDATE
def update_page_api():
    x = 0

#------------------------------------------------------------------------------
# INPUT

def getBrightness(processor):
    r = requests.get(ip_prefix + processor_array[processor].get("IP") + read(api["brightness"]))
    # r = requests.get(ip_array[processor] + read(api["brightness"]))
    brightness = r.content.decode("utf-8")
    brightness = brightness.split(":")
    brightness = brightness[1].split("}")
    return int(brightness[0])

def get_temperature(processor):
    r = requests.get(ip_prefix + processor_array[processor].get("IP") + read(api["temperature"]))
    temperature = r.content.decode("utf-8")
    temperature = temperature.split(":")
    temperature = temperature[1].split("}")
    return int(temperature[0])

def updateAll():
    number_of_processors = 0
    for processor in processor_array:
        if (len(processor.get("IP")) > 0):
            number_of_processors += 1

    for x in range(number_of_processors):
        update_button_brightness_text(x,getBrightness(x))
        update_button_temperature_text(x,get_temperature(x))

#------------------------------------------------------------------------------
# OUTPUT

def sendBrightness(unused_addr, processor, data):
    # float
    #-1 - 10000
    try:
        r = requests.put(ip_prefix + processor_array[processor].get("IP") + read(api["brightness"]), data={"data": data})
        getBrightness(processor)
        updateAll()
    except Exception as err:
        print("COULD NOT CONNECT TO PROCESSSOR " + str(processor) + " AT: " + processor_array[processor].get("IP"))


def sendTemperature(unused_addr, processor, data):
    # float
    #2000 - 11000
    r = requests.put(ip_prefix + processor_array[processor].get("IP") + read(api["temperature"]), data={"data": data})
    updateAll()


def sendDarkMagic(unused_addr, processor, data):
    # bool
    r = requests.put(ip_prefix + processor_array[processor].get("IP") + read(api["dark_magic"]), data={"data": data})


#------------------------------------------------------------------------------
# OVERRIDE
def sendBlackout(unused_addr, processor, data):
    # bool
    r = requests.put(ip_prefix + processor_array[processor].get("IP") + read(api["blackout"]), data={"data": data})
    # print(r.content)


def sendBlackoutFade(unused_addr, processor, data):
    # float
    #0.0 - 10.0
    r = requests.put(ip_prefix + processor_array[processor].get("IP") + read(api["blackout_fade"]), data={"data": data})
    # print(r.content)


def sendFreeze(unused_addr, processor, data):
    # bool
    r = requests.put(ip_prefix + processor_array[processor].get("IP") + read(api["freeze"]), data={"data": data})
    # print(r.content)


def sendTestPattern(unused_addr, processor, data):
    # bool
    r = requests.put(ip_prefix + processor_array[processor].get("IP") + read(api["test_pattern"]), data={"data": data})
    # print(r.content)


def sendTestPatternFormat(unused_addr, processor, data):
    # enum
    # from-input, standard-dynamic-range, perceptual-quantiser, hybrid-log-gamma
    r = requests.put(ip_prefix + processor_array[processor].get("IP") + read(api["test_format"]), data={"data": data})
    # print(r.content)


def sendTestPatternType(unused_addr, processor, data):
    # enum
    #brompton, brompton-overlay, red, green, blue, cyan, magenta, yellow, white, black,
    #grid, scrolling-grid, checkerbord, scrolling-cherkboard, colour-bars, gamma, gradient,
    #scrolling-gradient, strobe, smpte-bars, scrolling-smpte-bars, custom,
    #forty-five-degree-grid, scrolling-forty-five-degree-grid
    pattern_type = ["brompton", "brompton-overlay", "white", "red", "green", "blue", "cyan", "magenta", "yellow", "black",
    "grid", "scrolling-grid", "forty-five-degree-grid", "scrolling-forty-five-degree-grid", "checkerboard", "scrolling-checkerboard",
    "gradient", "scrolling-gradient", "colour-bars",  "strobe", "smpte-bars", "scrolling-smpte-bars", "custom-colour",  ]
    if str(data).isnumeric(): 
        r = requests.put(ip_prefix + processor_array[processor].get("IP") + read(api["test_type"]), data={"data": pattern_type[data]})
    else:
        r = requests.put(ip_prefix + processor_array[processor].get("IP") + read(api["test_type"]), data={"data": data})
