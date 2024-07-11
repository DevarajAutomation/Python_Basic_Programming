"""https://leetcode.com/problems/longest-common-prefix/description/"""

def longest_common_prefix(string):

    if len(string)==0:
        return ""
    
    base=string[0]

    for i in range(len(base)):
        for word in string[1:]:
            if i==len(word) or word[i] !=base[i]:
                return base[0:i]
            
    return base
strs = ["flower","flow","flight"]
print(longest_common_prefix(strs))

