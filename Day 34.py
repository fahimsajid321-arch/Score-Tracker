s1 = {112:92, 115:96, 667:85, 222:27, 124:80}
s2 = {123:86, 144:89, 143:100, 145:20, 124:82}
print(s1)
s1.update(s2) #Basically here all key value pairs of s2 has been added to s1 and value of 124 has been updated because it was present in s2 as well
print(s1)
s2.clear()
print(s2)
t =s1.pop(115)
print(t)
print(s1)
s1.popitem()
print(s1)
del(s1[123])
print(s1)
'''del s1
print(s1)'''
print(s1.keys())
for i in s1.keys():
    print(i)