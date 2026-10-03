s1 = {1, 2, 5, 7, 34, 25, 76}
s2 = {21, 34, 45, 23, 56, 76, 34}
#Union of Sets
print(s1.union(s2))
s1.update(s2)
print(s1)
#Intersection of sets "Common Values"
print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1)
#Symmetric Differece of Sets "Values that are not commen"
print(s1.symmetric_difference(s2))
s1.symmetric_difference_update(s2)
print(s1)
#Difference of Sets "Values that are not present in second set" like A-B
s1 = {1, 2, 5, 7, 34, 25, 76}
print(s1.difference(s2))
s1.difference_update(s2)
print(s1)

print(s1.isdisjoint(s2)) #Returns true of sets dont have anything in common
print(s1.issuperset(s2)) #Returns true if all values of s2 are present in s1
print(s2.issubset(s1))   #Returns true if s2 is the subset of s1
print(s1)
#Add method to add a single value in the set
s1.add(99)
print(s1)
#Update method to add multiple value in the set but has to be done in a way as done below
s1.update(s2)
print(s1)
#Remove method to remove specific vlaue from the set
s1.remove(56)
print(s1)
#Pop method to pop the single value from the set
item = s1.pop()
print(item)
print(s1)
#Del keyword to delete the set
del s1
#Clear method to remove all the entries from the set but it does not delete the set
s1 = {2, 99, 34, 5, 7, 76, 45, 21, 23, 25}
s1.clear()
print(s1)
#Method to check if item exists or not
if 45 in s2:
    print("Yes it is there")
else:
    print("No it is not there")
