import threading
import time
# import array as arr


from osc import *
from api import *
from companion import *

oscThread = threading.Thread(target=startOSC, args=())
oscThread.start()

companion_feedback_thread = threading.Thread(target=setup_companion, args=())
companion_feedback_thread.start()



# companionMark()


# def main():
#     print("hello")
#     time.sleep(2)
    # if input() == "exit":
        # stopOSC()



# sendBrightess(0,3000)
# sendTemperature(0,6000)
# sendDarkMagic(0,0)

# sendBlackout(0,0)

# while True:
#     # companionMark()
#     print()
#     main()


