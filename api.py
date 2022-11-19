import requests

from osc import *
from companion import *

numProcessors = 0

ip_prefix = "http://"
ip_array = ["http://192.168.0.105"]
max_brightness_array = [4000]

brightness_array = []
temperature_array = []

# TESSERA API VARIABLES
api_prefix = "/api"
# INPUT
api_refreshRate = api_prefix + "/input/active/refresh-rate"
api_input_res_height = api_prefix + "input/active/resolution/height"
api_input_res_width = api_prefix + "input/active/resolution/width"
api_input_portNumber = api_prefix + "input/active/source/port-number"
api_input_portType = api_prefix + "input/active/source/port-type"
# OUTPUT
api_brightness = api_prefix + "/output/global-colour/brightness"
api_temperature = api_prefix + "/output/global-colour/colour-temperature"
api_darkMagic = api_prefix + "/output/global-colour/dark-magic/enabled"

# OVERIDE
api_blackout = api_prefix + "/override/blackout/enabled"
api_blackout_fade = api_prefix + "/override/blackout/fade-time"
api_freeze = api_prefix + "/override/freeze/enabled"
api_test = api_prefix + "/override/test-pattern/enabled"
api_test_format = api_prefix + "/override/test-pattern/format"
api_test_type = api_prefix + "/override/test-pattern/type"

#------------------------------------------------------------------------------
# INPUT


def getBrightness(processor):
    r = requests.get(ip_array[processor] + api_brightness)
    brightness = r.content.decode("utf-8")
    brightness = brightness.split(":")
    brightness = brightness[1].split("}")
    
    return int(brightness[0])

#------------------------------------------------------------------------------
# OUTPUT


def sendBrightness(unused_addr, processor, data):
    # float
    #-1 - 10000
    r = requests.put(ip_array[processor] + api_brightness, data={"data": data})
    getBrightness(processor)
    print(r.content)


def sendBrightnessStep(unused_addr, processor, step, wait, held):
    r = requests.put(ip_array[processor] + api_brightness, data={"data": data})
    print(r.content)


def sendTemperature(unused_addr, processor, data):
    # float
    #2000 - 11000
    r = requests.put(ip_array[processor] +
                     api_temperature, data={"data": data})
    print(r.content)


def sendDarkMagic(unused_addr, processor, data):
    # bool
    r = requests.put(ip_array[processor] + api_darkMagic, data={"data": data})
    print(r.content)


#------------------------------------------------------------------------------
# OVERRIDE
def sendBlackout(unused_addr, processor, data):
    # bool
    r = requests.put(ip_array[processor] + api_blackout, data={"data": data})
    print(r.content)


def sendBlackoutFade(unused_addr, processor, data):
    # float
    #0.0 - 10.0
    r = requests.put(ip_array[processor] +
                     api_blackout_fade, data={"data": data})
    print(r.content)


def sendFreeze(unused_addr, processor, data):
    # bool
    r = requests.put(ip_array[processor] + api_freeze, data={"data": data})
    print(r.content)


def sendTestPattern(unused_addr, processor, data):
    # bool
    r = requests.put(ip_array[processor] + api_test, data={"data": data})
    print(r.content)


def sendTestPatternFormat(unused_addr, processor, data):
    # enum
    # from-input, standard-dynamic-range, perceptual-quantiser, hybrid-log-gamma
    r = requests.put(ip_array[processor] +
                     api_test_format, data={"data": data})
    print(r.content)


def sendTestPatternType(unused_addr, processor, data):
    # enum
    #brompton, brompton-overlay, red, green, blue, cyan, magenta, yellow, white, black,
    #grid, scrolling-grid, checkerbord, scrolling-cherkboard, colour-bars, gamma, gradient,
    #scrolling-gradient, strobe, smpte-bars, scrolling-smpte-bars, custom,
    #forty-five-degree-grid, scrolling-forty-five-degree-grid
    r = requests.put(ip_array[processor] + api_test_type, data={"data": data})
    print(r.content)
