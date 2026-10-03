# def greet(fx):
#     def mfx(*args, **kwargs):
#         print("Good Morning")
#         fx(*args, **kwargs)
#         print("Thanks for using this function")
#     return mfx



# def hello():
#     print("Hello world")


# hello() #if we use this method then we are required to put @greet before hello() function
# greet(hello)() #this is another method to use decorator function

# @greet
# def add(a, b):
#     print(a+b)

# add(1, 2)

import logging

def log_function_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"{func.__name__} with args = {args}, kwargs = {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"{func.__name__} returned {result}")
        return result
    return decorated
    
@log_function_call
def my_function(a, b):
    return a+b

a = my_function(1,2)
print(a)