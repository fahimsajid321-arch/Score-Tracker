#def sum(a,b):
#   s =a+b
#    print("Sum =", s)
#    return s


#sum(12,14)
#sum(15,17)
#sum(10101010,1010101001)//

'''def avg_nums(a,b,c):
    sum = a+b+c
    avg = sum /3
    return avg


average = avg_nums(12.00,14.00,14.00)
print(average)'''

'''def product(a=1, b) #wrong method of using default parameters, default argument will come at last
    product = a*b
    print(product)
    return product

product(,2)'''

'''def calc_len(list):
    lenth = len(list)
    print(lenth)
    return lenth

num1 = [1,2,3,4,5,6,6,7]
cities = ["Lahore", "Karachi", "Multan", "Gujranwala", "Sialkot"]
calc_len(cities)
calc_len(num1)'''

'''def prnt_list_elm(list):
        for item in list:
            print(item, end=" ")

num1 = [1,2,3,4,5,6,6,7]
cities = ["Lahore", "Karachi", "Multan", "Gujranwala", "Sialkot"]
prnt_list_elm(cities)
prnt_list_elm(num1)'''

'''def factorial(n):
    i= 1
    factorial = 1
    for i in range(1, n+1):
        factorial*=i
        i+=1
    print(factorial)
    return(factorial)


factorial(6)

def factorial(n):
    i= 1
    factorial = 1
    while i<=n:
        factorial*=i
        i+=1
    print(factorial)
    return(factorial)


factorial(6)'''

'''def converter(dollar):
    pkr = dollar * 280
    print(dollar, "USD =", pkr, "PKR")

converter(1000)'''

def fun(n):
    if(n%2==0):
        print("EVEN")
    else:
        print("ODD")


fun(4)