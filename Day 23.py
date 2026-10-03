l = [2, 4, 6, 12, 26, 22, 18, 54]
l.append(26) #To add an element at the end of list
print(l)
l.sort()     #To sort the list in ascending order
print(l)
l.reverse()  #To reverse the list
print(l)
print(l.index(12)) #Return the index of specific value in the list
print(l.count(2))  #Counts the number of times speciifc value exists in the list
m = l.copy()       #Copies the value from a list and returns a new list
print(m)
(l.insert(1,65))   #used to insert specific value at the specific index
print(l)
l.extend(m)        #Add the values of list to another list
print(l)
n = l + m          #Merges the elements of two lists
print(n)
n.sort(reverse=True)
print(n)