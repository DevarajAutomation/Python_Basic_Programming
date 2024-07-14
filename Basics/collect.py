import collections
from collections import Counter

arr=Counter()
arr.update(['B','B','A','B','C','A','B',
               'B','A','C'])



data=Counter()

data.update(["A",'B'])
print(data)
arr.update(data)
arr.subtract(data)
print(Counter(arr))
print(arr.values())
print(arr.keys())
print(arr.items())