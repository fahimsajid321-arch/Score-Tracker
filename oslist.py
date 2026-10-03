import os

folders = os.listdir("data")

for folder in folders:
    path = os.path.join("data", folder)
    if os.path.isdir(path):
        print(folder)
        print(os.listdir(path))
'''import os
folders = os.listdir("data")

#print(folders)

for folder in folders:
    print(folder)
    print(folders)
    print(os.listdir(f"data/{folder}"))'''
    