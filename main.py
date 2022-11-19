import threading
import time

from globals import *
from osc import *
from api import *
from companion import *

setup_page_api(verbose)
setup_page_osc(verbose)
setup_page_companion(verbose)

oscThread = threading.Thread(target=startOSC, args=())
oscThread.start()

# while True:
    # getAll()
    # time.sleep(1)
#     update_page_api()
#     update_page_osc()
#     update_page_companion()
#     startOSC()

#     print(numProcessors)

#     time.sleep(1)

#     # update_button_brightness_text()
