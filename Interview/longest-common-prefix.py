def longest_common_prefix(strs):

    if len(strs)==0:
        return ""

    base=strs[0]
    for i in range(len(base)):
        for word in strs[1:]:
            if i==len(word) or word[i] !=base[i]:
                return base[0:i]

    return base

strs = ["flower","flow","flight"]
print(longest_common_prefix(strs))
