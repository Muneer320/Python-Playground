import os


path = 'C:\\Users\\munee\\desktop'
os.chdir(path)

for x in range(1001):
    os.mkdir(path + f"\\{x}")

print('Done!!')