class Math:
    def __init__(self, num):
        self.num = num

    def addtonum(self, n):
        self.num = self.num + n
        return self.num

    @staticmethod
    def add(a, b):
        print(a + b)

a = Math(5)
print(a.addtonum(6))
a.add(4,5)
Math.add(2,4)