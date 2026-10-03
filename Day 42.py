marks = [23, 24, 25, 18, 56, 76, 78, 89]

'''index = 0
for mark in marks:
    print(mark)
    if(index == 7):
        print("Faheem Great")
    index = index + 1'''

'''for index, mark in enumerate(marks):
    print(index, mark)
    if(index==7):
        print("Faheem Great")'''

for index, mark in enumerate(marks,start=1):
    print(index, mark)
    if(index==7):
        print("Faheem Great")

