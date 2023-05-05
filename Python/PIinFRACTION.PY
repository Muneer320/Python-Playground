from joblib import PrintTime
from torch import true_divide


import time

num = 1
run = True

while run:
    denominator = num / 3.141592
    print(num, denominator)
    
    # if denominator == int(denominator):
    if denominator - 3.141592 < 0.0000001:
        print(f"The value is: {num}/{int(denominator)}")
        run = False
    else:
        num += 1