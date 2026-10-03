import functools
import time

@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(3) #This is here to add day of 3 seconds before the function executes the next statement
    return n*5

print(fx(5)) #here this will take exactly 3 seconds to return the result due to time.sleep method
print("Done for 5")
print(fx(10))
print("Done for 10")
print(fx(15))
print("Done for 15")

print(fx(5)) #here this will take exactly 3 seconds to return the result due to time.sleep method
print("Done for 5")
print(fx(10))
print("Done for 10")
print(fx(15))
print("Done for 15")