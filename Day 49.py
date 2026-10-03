#Reading a file
'''f = open('myFile.txt','r')
print(f)
text = f.read()
print(text)
f.close()'''

#Writing a file
'''f = open("myFile.txt", "w")
text = f.write("Hello World")
print(text)
f.close()
'''
#Appending a file
'''f = open("myFile.txt", "a")
text = f.write("Hello World")
print(text)
f.close()'''

f = open("myFile.txt", "a")
with open("myFile.txt", "a"):
    f.write("Hey I am in using with!!")