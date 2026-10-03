import time
# def usingWhile():
#     i = 0
#     while i <= 50000:
#         print(i)
#         i = i + 1

# def usingFor():
#     for i in range(50001):
#         print(i)
# t1= time.time()
# usingWhile()
# t2 = time.time()
# usingFor()
# print(time.time() - t1)
# time.sleep(5)
# print("After 5 Seconds")
# print(time.time() - t2)

t = time.localtime()
formatted_time = time.strftime("%Y - %m - %d -- %H : %M : %S", t)
print(formatted_time )



