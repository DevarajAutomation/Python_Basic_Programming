"""https://www.hackerrank.com/challenges/staircase/problem"""

#n-length of input
def strair_case(n):

    for i in range(1,n+1):

        #print((n-i)* " " + i * "#")
        print((2*i*'#') + "" * ( n-i))


n=9

strair_case(9)