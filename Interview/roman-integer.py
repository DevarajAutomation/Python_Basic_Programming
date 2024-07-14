"""https://leetcode.com/problems/roman-to-integer/description/"""


def roman_integer(s):
    total = 0
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000

    }

    for i in range(len(s) - 1):
        if roman_dict[s[i]] < roman_dict[s[i + 1]]:
            total -= roman_dict[s[i]]

        else:
            total += roman_dict[s[i]]

    return total + roman_dict[s[-1]]

strs="MCMXCIV"
print(roman_integer(strs))