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
    update_button_id_text()
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

    except Exception as err:
        exit_program("COULD NOT CONNECT TO COMPANION\nCHANGE SETTINGS.JSON OR CHECK COMPANION")
    
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

def update_button_id_text():
    print()
    # ip_address = ip_prefix + settings.get("COMPANION IP") + ":" + settings.get("COMPANION PORT")
    # button_number = settings.get("FEEDBACK BUTTON")
    # for i, processor in enumerate(processor_array):
    #     page_number = str(processor_array[i].get("PAGE"))
    #     ident = str(processor_array[i].get("PROCESSOR"))
    #     r = requests.get(ip_address + "/style/bank/" + page_number + "/" + button_number + "/?text=" + "ID" + "\\n" + ident, auth=('user', 'pass'))
    #     r = requests.get(ip_address + "/style/bank/" + page_number + "/" + button_number + "/?size=" + "24", auth=('user', 'pass'))


def update_button_brightness_text(processor,brightness):
    ip_address = ip_prefix + settings.get("COMPANION IP") + ":" + settings.get("COMPANION PORT")
    button_number = str(int(settings.get("FEEDBACK BUTTON")) + 1)
    page_number = str(processor_array[processor].get("PAGE"))
    percent = str(int(normalize(brightness,0,processor_array[processor].get("MAX_BRIGHTNESS"),0,100)))
    r = requests.get(ip_address + "/style/bank/" + page_number + "/" + button_number + "/?text=" + "BRIGHT" + "\\n" + str(brightness) + "\\n" + percent + "%", auth=('user', 'pass'))
    r = requests.get(ip_address + "/style/bank/" + page_number + "/" + button_number + "/?size=" + "14", auth=('user', 'pass'))

def update_button_temperature_text(processor,temperature):
    ip_address = ip_prefix + settings.get("COMPANION IP") + ":" + settings.get("COMPANION PORT")
    button_number = str(int(settings.get("FEEDBACK BUTTON")) + 2)
    page_number = str(processor_array[processor].get("PAGE"))
    r = requests.get(ip_address + "/style/bank/" + page_number + "/" + button_number + "/?text=" + "TEMP" + "\\n" + str(temperature), auth=('user', 'pass'))
    r = requests.get(ip_address + "/style/bank/" + page_number + "/" + button_number + "/?size=" + "18", auth=('user', 'pass'))
