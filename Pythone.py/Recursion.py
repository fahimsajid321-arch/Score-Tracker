'''def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1)*n
print(fact(6))'''

#Practice 1
'''def sum(n):
    if (n==0):
        return 0
    return sum(n-1) + n
    
    
add=sum(5)
print(add)'''
#Pratice 2
def print_list(list, idx=0):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list, idx+1)

num = [1,2,3,4,5,6,7]
print_list(num)