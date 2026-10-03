import os

# os.mkdir("data")

# if(not os.path.exists("data")):
#     os.mkdir("data")

# for i in range(1, 101):
#     if(not os.path.exists("data")):
#         os.mkdir(f"data/day{i}")
#     os.rename(f"data/day{i}", f"data/Tutorial {i}")  
folders = os.listdir("data")
print(folders)

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))
