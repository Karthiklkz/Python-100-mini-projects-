import pywhatkit 

# pip install pywhatkit

import time


contacts = ["+918098627513", "+916382399519"]
message = "Hi! This is a bot message."

for contact in contacts:
    pywhatkit.sendwhatmsg_instantly(contact, message, wait_time=10, tab_close=True)
    time.sleep(10)  # Wait to avoid too many open tabs

