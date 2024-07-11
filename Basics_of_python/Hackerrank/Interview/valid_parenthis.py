"""https://leetcode.com/problems/valid-parentheses/description/"""

def valid_paraenthisis(s):

    stack=[]

    pairs={
        '(':')',
        "{":"}",
        "[":"]"
    }

    for bracket in s:
        if bracket in pairs:
            stack.append(bracket)
        elif len(stack)==0 or bracket != pairs[stack.pop()]:
            return False
        
    return len(stack)==0

s = "()[]{}"

print(valid_paraenthisis(s))

