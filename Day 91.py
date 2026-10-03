def generator():
    for i in range(1000):
        yield i

gen = generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
for j in gen:
    print(j)