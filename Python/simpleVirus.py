import os


for x in range(1001):
    os.makedirs(f"C:/Users/munee/Desktop/{x}")

# To reverse the effect

# for x in range(1001):
#     try:
#         os.rmdir(f"C:/Users/munee/Desktop/{x}")
#     except:
#         pass