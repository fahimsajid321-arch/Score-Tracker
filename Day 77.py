# class Point:
#     def __init__(self,i, j):
#         self.i = i
#         self.j = j
#     def __add__(self, x):
#         return Point(self.i+x.i, self.j+x.j)
# p1 = Point(2, 3)
# p2 = Point(4, 5)
# p3 = p1 + p2
# print(p3.i, "," , p3.j)

class Vector:
    def __init__(self,i,j, k):
        self.i = i
        self.j = j
        self.k = k
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    def __add__(self,x):
        return Vector(self.i + x.i, self.j + x.j, self.k +x.k)
v1 = Vector(2,3,4)
print(v1)
v2 = Vector(5,6,7)
print(v2)
print(v1 + v2)
