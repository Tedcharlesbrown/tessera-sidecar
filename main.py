import threading
import time

from globals import *
from settings import *
from osc import *
from api import *
from companion import *

sleep_time = 1

setup()

time.sleep(sleep_time)

setup_page_api(verbose)

time.sleep(sleep_time)

setup_page_osc(verbose)

time.sleep(sleep_time)

setup_page_companion(verbose)

time.sleep(sleep_time)

oscThread = threading.Thread(target=startOSC, args=())
oscThread.start()

time.sleep(sleep_time)

print(appName + " IS NOW RUNNING!")
print(appCredit)
print(appVersion)

while True:
#     update_page_api()
#     update_page_osc()
    update_page_companion()

#     time.sleep(1)

#     # update_button_brightness_text()
