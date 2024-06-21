import math

"""https://www.hackerrank.com/challenges/kangaroo/problem"""

def kangaroo_jump(x1,v1,x2,v2):

    if v1==v2:
        if x1==x2:
            return 'YES'
        else:
            return 'NO'
        
    else:
        n=(x1-x2)/(v2-v1)

        if n >0 and n.is_integer():
            return 'YES'
        else:
            return 'NO'
        
print(kangaroo_jump(0,3,4,2))