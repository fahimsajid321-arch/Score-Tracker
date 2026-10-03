import os
# os.rename("clutterFolder/file.txt", "clutterFolder/7.txt")

files = os.listdir("clutterFolder")
j = 1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"clutterFolder/{file}", f"clutterFolder/{j}.png")
        j = j + 1