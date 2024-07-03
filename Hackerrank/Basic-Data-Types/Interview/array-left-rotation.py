"""https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem"""

a=[1,2,3,4,5]
k=3
result= a[k:] + a[:k]
print(result)
