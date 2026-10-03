#Here we are taking a list as an input and printing the cube of each element of list and getting a new list using the loop
# MAP
# def cube(x):
#     return x*x*x
# l = [1,2,3,4,5,6]
# # newl = []
# # for item in l:
# #     newl.append(cube(item))
# newl = list(map(cube, l))
# print(newl)

# # FILTER
# def filter_fuc(a):
#     return a>2

# newnewl = list(filter(filter_fuc, l))
# print(newnewl)

from functools import reduce

l = [1,2,3,4,5]
sum = reduce(lambda x,y:x+y, l)

print(sum)




