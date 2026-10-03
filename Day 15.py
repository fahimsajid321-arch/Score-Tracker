import time
times = time.strftime("%H:%M:%S")
print(times)
Hours = int(time.strftime("%H"))
print(Hours)
Minutes = int(time.strftime("%M"))
print(Minutes)
Seconds = int(time.strftime("%S"))
print(Seconds)

YourHours = int(input("Enter Your Hours:"))
if(YourHours>=0 and YourHours<=12):
    print("Good Morning Sir!")
elif(YourHours>12 and YourHours<=16):
    print("Good Afternoon Sir!")
elif(YourHours>16 and YourHours<=19):
    print("Good Evening Sir!")
else:
    print("Good Night Sir!")