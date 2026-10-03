class Myclass:
    def __init__(self, value):
        self._value = value


    def show(self):
        print(f"Value is {self._value}")
        return self._value

    @property
    def ten_value(self):
        return 10*self._value
    
    @ten_value.setter
    def ten_value(self, new_value):
        self._value = new_value
        return new_value

obj = Myclass(10)
obj.show()
print(obj.ten_value)
obj.ten_value = 50
obj.show()