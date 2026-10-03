#This is the example how tuple is passed as an argument in case of function
def average(*numbers):  #This is variable length argument examle and here python will consider this a tuple any number cna be given to calculate their average and any number of arguments or parameters cna be passed this case
    sum = 0
    for i in numbers:
        sum = sum + i
    #print("Average is:", sum/len(numbers))
    return sum/len(numbers)

c = average(5,12,15)
print(c)


#Now this is the example how dictonary can be taken as argumments
'''def namesOfIndl(**names):
    print("Hello", names["myName"], names["friendName"],names["brotherName"])

namesOfIndl(myName="Faheem",friendName="AWAIS",brotherName="Hamza")'''