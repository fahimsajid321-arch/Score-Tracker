f = int(input("Enter the number of words you want to decode: "))
nword = []
for i in range(f):
    g = input("Enter your word: ")
    if len(g) <= 3:
        nword.append(g[::-1])              # reverse short words
    else:
        g = g[3:-3]
        finalWord = g[-1]+g[0:-1]
        nword.append(finalWord)
        print(nword)

print(" ".join(nword))