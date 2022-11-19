import requests
import time

from globals import *
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
    set_companion_buttons()
    # while True:
        # update_page_companion()

    if verbose:
        print("COMPANION PAGE SETUP")


def set_companion_buttons():
    r = requests.get(
        internalAddress + "/style/bank/99/29/?text=" + appName, auth=('user', 'pass'))
    r = requests.get(internalAddress +
                     "/style/bank/99/29/?size=" + "14", auth=('user', 'pass'))

    r = requests.get(internalAddress + "/style/bank/99/30/?text=" +
                     appVersion, auth=('user', 'pass'))
    r = requests.get(internalAddress +
                     "/style/bank/99/30/?size=" + "14", auth=('user', 'pass'))

    r = requests.get(internalAddress + "/style/bank/99/31/?text=" +
                     appCredit, auth=('user', 'pass'))
    r = requests.get(internalAddress +
                     "/style/bank/99/31/?size=" + "14", auth=('user', 'pass'))

    r = requests.get(internalAddress + "/style/bank/99/32/?text=" +
                     str(heartbeat), auth=('user', 'pass'))
    r = requests.get(internalAddress +
                     "/style/bank/99/32/?size=" + "14", auth=('user', 'pass'))

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


def setup_button_text(unused_addr, processor, bank, button):
    # get total number of feedback buttons
    global numFeedback
    if numFeedback <= processor:
        numFeedback = processor + 1
        # assign new arrays
        bank_array.insert(processor, bank)
        button_array.insert(processor, button)

        # clear all previously used arrays
        if len(bank_array) > numFeedback:
            i = numFeedback
            while i < len(bank_array):
                bank_array.pop(i)
                button_array.pop(i)


def update_button_brightness_text(processor,brightness):
    page_number = str(processor + 1)
    percent = str(int(normalize(brightness,0,max_brightness_array[processor],0,100)))
    r = requests.get(internalAddress + "/style/bank/" + page_number + "/" + "2" + "/?text=" + "BRIGHT " + str(brightness) + "    " + percent + "%", auth=('user', 'pass'))
    r = requests.get(internalAddress + "/style/bank/" + page_number + "/" + "2" + "/?size=" + "14", auth=('user', 'pass'))

def update_button_temperature_text(processor,temperature):
    page_number = str(processor + 1)
    r = requests.get(internalAddress + "/style/bank/" + page_number + "/" + "3" + "/?text=" + "TEMP " + str(temperature), auth=('user', 'pass'))
    r = requests.get(internalAddress + "/style/bank/" + page_number + "/" + "3" + "/?size=" + "18", auth=('user', 'pass'))
