"""https://www.hackerrank.com/challenges/list-comprehensions/problem"""

def cuboid(x,y,z,n):

    return [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n]



x,y,z,n=2,2,2,2

print(cuboid(x,y,z,n))