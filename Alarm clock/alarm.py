import datetime
import time
import winsound

alarm_time = "18:45:00"
print(f"Setting alarm for {alarm_time}...")

while True:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    if current_time == alarm_time:
        # print("⏰ Alarm ringing now!")
        winsound.Beep(2000, 1000)  # frequency (Hz), duration (ms)
        break
    time.sleep(1)
