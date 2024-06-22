"""https://www.hackerrank.com/challenges/the-hurdle-race/problem"""


def hurdle_race(n,height):

    dose=0

    if height > max(n):
        return 0
    else:
        dose+=max(n)-height

        return dose
    
n=[1,6,3,5,2]
h=4
n1=[2,5,4,5,2]
h1=7
print(hurdle_race(n1,h1))