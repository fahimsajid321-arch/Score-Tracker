def encoder(x):
    prefix = input("Enter three random alphabets as prefix:")
    if len(prefix)>3:
        raise ValueError("Not more than 3 characters are allowed")
    suffix = input("Enter three random alphabets:")
    if len(suffix)>3:
        raise ValueError("Not more than 3 characters are allowed")
    d = prefix+x[1:len(x)]+x[0]+suffix
    return d

f = input("Enter your statement: ")
s = f.split()
print(s)
nword =[]
for i in s:

    if len(i) <= 3:
        nword.append(i[::-1])             # reverse short words
    else:
        nword.append(encoder(i))
    print(nword)
    
print(" ".join(nword))

