"""https://www.hackerrank.com/challenges/apple-and-orange/problem"""


def apple_orange(s,t,a,b,apples,oranges):

    apple_count=0
    orange_count=0

    for apple in apples:

        if s<= a+apple <=t:

            apple_count +=1

    for orange in oranges:
        if s<= b + orange <=t:
            orange_count +=1

    return (apple_count,orange_count)