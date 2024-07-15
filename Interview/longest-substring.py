def longest_substring(strs):
    length=0
    seen={}
    l=0

    for r in range(len(strs)):
        char=strs[r]
        if char in seen and seen[char] >=l:
            l=seen[char] +1
        else:
            length=max(length,r-l+1)

        seen[char]=r
    return length

strs='abcdcefg'
print(longest_substring(strs))
