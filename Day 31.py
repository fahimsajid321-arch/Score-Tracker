faheem = {}          #Its not an empty set, its an empty dictonary
print(type(faheem))

faheem = set()         #Its not an empty dic, its an empty set
print(type(faheem))

s = {2,3,5,7,2,4,4}
print(s)               #Set does not contain repitative values it will merge values that are their in the set for more than once

items = {2, 4, 56, "Faheem", "Bilal", 6.0} #Set can have elements of different data type
print(items)         #Sets do not maint order they unordered and they will return output with different order each time they are printed

for i in items:
    print(i)