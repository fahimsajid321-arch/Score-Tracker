f = open("myFile.txt", "r")  #Opening of a file
for i in range(1,4):         #Reading through the lines entry by entry eacg line
    line = f.readline()
    if not line:
        break
    m1 = line.split(",")[0]  #first entry if line 
    m2 = line.split(",")[1]  #Second entry of line 
    m3 = line.split(",")[2]  #Third entry of line

    print(f"Marks of student {i} in Math: {m1}") #For first entry 
    print(f"Marks of student {i} in Math: {m2}") #For second entry
    print(f"Marks of student {i} in Math: {m3}") #   ''
    print(line)


f1 = open("myFile2.txt", "w")
lines = ["line 1\n", "line 2\n", "line 3\n"]
f1.writelines(lines)
f1.close()