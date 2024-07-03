"""https://www.hackerrank.com/challenges/diagonal-difference/problem"""



def diag_diff(ar):

    diff=0
    for i in range(len(ar)):

        diff += ar[i][i] - ar[i][len(ar)-i-1]

    return abs(diff)