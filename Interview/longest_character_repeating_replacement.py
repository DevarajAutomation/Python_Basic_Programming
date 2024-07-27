def longest_repeating_replacement(s,k):
    freq=0
    res=0
    left=0
    char={}

    for right in range(len(s)):
        char[s[right]]=char.get(s[right],0)+1
        freq=max(freq,char[s[right]])

        while (right-left+1)-freq > k:
            char[s[left]] -=1
            left +=1

        res=max(res,right-left+1)

    return res

s = "ABAB"
k = 2

print(longest_repeating_replacement(s,k))

