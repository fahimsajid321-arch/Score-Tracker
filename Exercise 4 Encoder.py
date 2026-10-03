def encoder(x):
    prefix = input("Enter three random alphabets as prefix:")
    if len(prefix)>3:
        raise ValueError("Not more than 3 characters are allowed")
    suffix = input("Enter three random alphabets:")
    if len(suffix)>3:
        raise ValueError("Not more than 3 characters are allowed")
    d = prefix+x[1:len(x)]+x[0]+suffix
    return d

f = int(input("Enter the number of words you want to encode: "))
nword =[]
for i in range(f):
    g = input("Enter your word: ")

    if len(g) <= 3:
        nword.append(g[::-1])             # reverse short words
    else:
        nword.append(encoder(g))
    print(nword)
    
print(" ".join(nword))   