import math
import random 

a = input("Enter the letters >>> ") 

ltrlenlst = [x for x in range(1, len(a)+1)]
ltrlen = math.prod(ltrlenlst) 

def add(a, ltrlen):
    res = [] 

    while len(res) != ltrlen:
        newA = ''.join(random.sample (a,len(a))) 
    if newA not in res:
        res.append(newA) 

    return res 

res = add(a, ltrlen)
res.sort()

print("Total no. of combinations: " ,len(res))
for x in res:
    print(x)