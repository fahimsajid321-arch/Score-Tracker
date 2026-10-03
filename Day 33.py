dic = {
    'name': "Faheem",
    'PA No': 62457,
    'Age' :  26,
    'Course': "143 Long Course",
    "Unit"  : "9 Sig Bn",
    "Degree"  : "EE-61"
}   #This is the method of creating the dictonary

print(dic) #This will print entire dictonary
print(dic.get("account"))  #Returns specific value against key that is mentioned  #This method does not return error if key os not present in the dictonary, it returns "None"
print(dic["PA No"])   #Returns specific value against key that is mentioned  #This method returns error if key is not present in the dictonary

print(dic.keys())   #It returns all they keys, only keys
print(dic.values()) #It returns all the values, only values

for key in dic.keys(): #Printing keys and values using loop
    print(key,dic[key])

for key in dic.keys():  #Printing Keys and values using f-string and loop
    print(f"Value corresponding to this {key} is {dic[key]}")

print(dic.items()) #Returns dictonary as key and value pairs
for i,j in dic.items(): 
    print(f"The value corresponding to this {i} is {j} ")