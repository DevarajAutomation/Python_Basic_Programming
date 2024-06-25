"""https://www.hackerrank.com/challenges/write-a-function/problem"""

def leap_year(year):

    leap= year%4==0 and (year % 100 !=0 or year % 400 ==0)

    return leap



y_1=2003
y_2=2011
y_3=2012

print(leap_year(y_1))
print(leap_year(y_2))
print(leap_year(y_3))

