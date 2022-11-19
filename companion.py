import requests
import time

internalAddress = "http://127.0.0.1:8888"
appName = "TESSERA SIDECAR"
appVersion = "DEV BUILD v.01"
appCredit = "TED CHARLES BROWN"

update = False
heartbeat = 0

bank_array = []
button_array = []


def setup_companion():
    set_companion_buttons()
    while True:
        update_companion()
    # print(r.content)


def update_companion():
    global update, heartbeat
    if int(time.time()) % 10 == 0:
        if update == True:
            set_companion_buttons()
            update = False
            heartbeat += 1
    else:
        update = True


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
    print(bank_array)


# def set_button_text(processor):
#     global brightness_array
#     r = requests.get(internalAddress + "/style/bank/" + bank_array[processor] + "/" + button_array[processor] + "/?text=" + brightness_array[processor], auth=('user', 'pass'))
    # r = requests.get(internalAddress + "/style/bank/99/32/?size=" + "14", auth=('user', 'pass'))
