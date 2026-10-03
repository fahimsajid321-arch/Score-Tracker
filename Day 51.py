f = open("myFile.txt", "r")
print(type(f))
f.seek(6) #seek() will move the pointer to 6th position and then we can mov fwd and backward from there
current_loc = f.tell()
print(current_loc)
data = f.read(6) #Will raed 5 bytes after skipping 6 bytes 
# data1 = f.read(5) #Will raed 5 bytes after skipping 6 bytes 
# data2 = f.read(-10)  #Negative indexing isnt allowed so it isnt possible to print (-10) bytes
current_loc = f.tell()
print(data)
print(current_loc)
# print(data1)
# print(data2)

with open("sample.txt", "w") as f:
    f.write("Hello World")
    f.truncate(5) #Use for reducing the file size argument will be number of bytes that we want from current loc of pointer

with open("sample.txt", "r") as f:
    print(f.read())