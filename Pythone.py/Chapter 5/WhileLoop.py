#a = 1
#while a<=5:
#    print("Hello")
#    a=a+1
#print(a)
#Practice Question 1
#num=1
#while num<=100:
#    print(num)
#    num+=1
#print ("Value has exceeded 100")
#Prctice Question 2
#num=100
#while num>=1:
#    print(num)
#    num-=1
#print ("Loop ended")
#Practice Question 3
#n = 2
#m = 1
#while m<=10:
#    P=m*n
#    print(n, "*", m, "=", P)
#    m+=1
#Practice Question 4
#list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#lenth = len(list) 
#count = 0
#while count<lenth:
#    print(list[count])
#    count+=1

#Practice Question 4
#list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#lenth = len(list) - 1
#count = 0
#while count<=lenth:
#    print(list[count])
#    count+=1

#Practice Question 5
#tup1 = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
#x = int(input("Enter a number: "))
#i = 0
#while i < len(tup1):
#    if (tup1[i]==x):
#        print("Number exists at index", i)
#    i+=1

i = 0
while i<= 100:
    if(i%2!= 0):
        i+=1
        continue
    print(i)
    i+=1