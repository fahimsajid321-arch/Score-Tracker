#list = ["Potato", "Brinjal"]

#for val in list: #
#    print(val)

#tup = (1, 2, 3, 4, 5)

#for num in tup:
#    print(num)

#str = "FaheemSajid"
#for char in str:
#    if(char == "m"):
#        print("m found")
#        break
#    print(char)
#else:
#    print("Search ended")

#Practice Question 1
#list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#for val in list:
#    print(val)

#Practice Question 2
#tup1 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

#num1 = int(input("Enter a number: "))
#idx = 0
#for val in tup1:
#    if(val == num1):
#        print(num1,"is found at", idx)
#        break
#    idx+=1
#else:
#    print("Number does not exist")

# Range() Function example
#num1 = int(input("Enter a Number:"))
#seq = range(1,11)
#for i in seq:
#    p = i*num1
#    print(num1, "x", i, "=", p)

#practice Question
#n = 5
#product = 1
#i = 1
#while i<=n:
#
#    
#    product*=i
#    i+=1
#print (product)

n = 5
product = 1
for i in range(1, n+1):
    product*=i
    
print(product)
