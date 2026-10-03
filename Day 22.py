marks = [2, 3, 6, "Faheem", True]
print(marks)
print(type(marks))

#Accessing the different indexes of list
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])

#Negative Indexing
print(marks[-3])
print(marks[len(marks)-3])
print(marks[5-3])
print(marks[2])

#Checking for certain value or entry in the lis
if 7 in marks:
    print("Yes")
else:
    print("No")

if 6 in marks:
    print("Yes")
else:
    print("No") 

if "arry" in "Harry":   #Same thing applies for string as well
    print("Yes")
else:
    print("No")

print(marks)
print(marks[:])    
print(marks[1:])
print(marks[:len(marks)])
print(marks[1:6:2])

#List Comprehension
lst = [i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i%2==0]
print(lst)
