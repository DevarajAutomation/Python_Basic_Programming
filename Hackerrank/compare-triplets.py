"""https://www.hackerrank.com/challenges/compare-the-triplets/problem"""

a=[1,2,3]
b=[2,3,4]

#a=list(map(int,input().split()))
#b=list(map(int,input().split()))

a_point=sum([ (1 if a[i] > b[i] else 0) for i in range(3)])
b_point=sum([ (1 if a[i] < b[i] else 0) for i in range(3)])

print(a_point,b_point)
