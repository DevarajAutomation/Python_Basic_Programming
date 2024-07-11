"""https://leetcode.com/problems/roman-to-integer/description/"""

def convert_roman_to_integer(s):

    roman={

        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    total=0
    for i in range(len(s)-1):

        if roman[s[i]] < roman[s[i+1]]:
            total -=roman[s[i]]
        else:
            total +=roman[s[i]]

    return total + roman[s[-1]]

s="IDI"

print(convert_roman_to_integer(s))