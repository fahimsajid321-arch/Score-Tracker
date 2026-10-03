tup = ("Pakistan", "india", "Bangladesh", "China", "Srilank" )
list1 = list(tup)
print(list1)
list1.append("Nepal")
print(list1)
list1.insert(2,"Bhutan")
print(list1)
list1[1]="Pajeets"
print(list1)
tup = tuple(list1)
print(tup)

if "Pakistan" in tup:
    print("Yes this great country exists")
print(tup.index("Bangladesh"))