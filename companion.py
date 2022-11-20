import requests
import time

from globals import *
from settings import *
from functions import *
from api import *
from osc import *

update = False
heartbeat = 0

bank_array = []
button_array = []

#------------------------------------------------------------------------------
# SETUP
def setup_page_companion(verbose):
    global settings
    settings = get_settings()
    set_companion_buttons()
    # while True:
        # update_page_companion()
    if verbose:
        print("COMPANION PAGE SETUP")


def set_companion_buttons():
    ip_address = ip_prefix + settings.get("COMPANION IP") + ":" + settings.get("COMPANION PORT")
    settings_page = settings.get("SETTINGS PAGE")

    print("CONNECTING TO COMPANION AT: " +  ip_address)

    try:
        r = requests.get(ip_address + "/style/bank/" + str(settings_page) + "/29/?text=" + appName, auth=('user', 'pass'))
        r = requests.get(ip_address + "/style/bank/" + str(settings_page) + "/29/?size=" + "14", auth=('user', 'pass'))

        r = requests.get(ip_address + "/style/bank/" + str(settings_page) + "/30/?text=" + appVersion, auth=('user', 'pass'))
        r = requests.get(ip_address + "/style/bank/" + str(settings_page) + "/30/?size=" + "14", auth=('user', 'pass'))

        r = requests.get(ip_address + "/style/bank/" + str(settings_page) + "/31/?text=" + appCredit, auth=('user', 'pass'))
        r = requests.get(ip_address + "/style/bank/" + str(settings_page) + "/31/?size=" + "14", auth=('user', 'pass'))

        r = requests.get(ip_address + "/style/bank/" + str(settings_page) + "/32/?text=" + str(heartbeat), auth=('user', 'pass'))
        r = requests.get(ip_address + "/style/bank/" + str(settings_page) + "/32/?size=" + "14", auth=('user', 'pass'))
    except:
        print("COULD NOT CONNECT TO COMPANION!")
        input("Press ENTER to close")
#------------------------------------------------------------------------------
# UPDATE

def update_page_companion():
    global update, heartbeat
    if int(time.time()) % 10 == 0:
        if update == True:
            set_companion_buttons()
            update = False
            heartbeat += 1
    else:
        update = True


numFeedback = 0


def update_button_brightness_text(processor,brightness):
    page_number = str(processor_array[processor].get("PAGE"))
    percent = str(int(normalize(brightness,0,processor_array[processor].get("MAX_BRIGHTNESS"),0,100)))
    r = requests.get(internalAddress + "/style/bank/" + page_number + "/" + "2" + "/?text=" + "BRIGHT" + "\\n" + str(brightness) + "\\n" + percent + "%", auth=('user', 'pass'))
    r = requests.get(internalAddress + "/style/bank/" + page_number + "/" + "2" + "/?size=" + "14", auth=('user', 'pass'))

def update_button_temperature_text(processor,temperature):
    page_number = str(processor_array[processor].get("PAGE"))
    r = requests.get(internalAddress + "/style/bank/" + page_number + "/" + "3" + "/?text=" + "TEMP" + "\\n" + str(temperature), auth=('user', 'pass'))
    r = requests.get(internalAddress + "/style/bank/" + page_number + "/" + "3" + "/?size=" + "18", auth=('user', 'pass'))
