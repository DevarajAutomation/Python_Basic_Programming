"""https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/description/"""


ar=[3,6,9]
min=0

for i in range(len(ar)):
    if ar[i] %3==0:
        min +=0
    elif ar[i] < 3 and 3-ar[i] ==1:
        ar[i] +=1
        min +=1
    elif ar[i] < 3 and 3-ar[i] ==2:
        ar[i] -=1
        min +=1
    elif 3 - ar[i]%3==1:
        ar[i] -=1
        min +=1
    else:
        ar[i] +=1
        min +=1

print(min)


