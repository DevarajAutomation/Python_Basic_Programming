from collections import defaultdict

d=defaultdict(int)

L=[1,2,3,2,3,1,4,5]

for i in L:
    d[i]+=1

print(d)