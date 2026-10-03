import win32com.client
import time

speaker = win32com.client.Dispatch("SAPI.SpVoice")

# Flag 1 (SVEFIsXML / default) | Flag 1 (SVSFlagsAsync) = 1
# Passing 1 enables Asynchronous mode
l = ["Faheem", "Bilal", "Awais"]
while True:
    for i in l:
        speaker.Speak(f"Shoutout to {i}")
        time.sleep(1)
   


# Python continues running immediately while audio plays
# for i in range(5):
#     print(f"Doing other work... {i}")
#     time.sleep(1)