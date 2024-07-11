"""https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/solutions/"""

def first_occurance(heystick,needle):

    if len(heystick) < len(needle):
        return -1
    
    for i in range(len(heystick)):
        if heystick[i:i+len(needle)]==needle:
            return i
        
    return -1

haystack = "leetcode"
needle = "leeto"


print(first_occurance(haystack,needle))

    