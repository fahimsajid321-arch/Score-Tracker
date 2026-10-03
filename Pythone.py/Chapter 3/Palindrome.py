list1 = [1, 2, 3, 2, 1]
list2 = list.copy(list1)
list.reverse(list2)
print(list2)
if (list1 == list2):
    print("Palindrome")
else:
    print("Not a Palindrone")

    
