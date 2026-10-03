import win32com.client
import time

current_time = time.strftime("%H : %M : %S")
hours = time.strftime("%H")
water_reminder = win32com.client.Dispatch("SAPI.SpVoice")
l = "Drink Water"
print(current_time)
while 8 <= int(hours) < 22:
    water_reminder.Speak(l)
    print(l)
    time.sleep(10)
    hours = time.strftime("%H")
