from collections import defaultdict

def count_triplets(arr,r):
    arr2=defaultdict(int)
    arr3=defaultdict(int)
    count=0
    for i in arr:
        count += arr3[i]
        arr3[i*r] += arr2[i]
        arr2[i*r] +=1
    return count

ar=[1,4,16,64]
r=4

print(count_triplets(ar,r))