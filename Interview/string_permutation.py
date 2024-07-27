def string_permutation(s1, s2):
    if len(s1) > len(s2):
        return False

    s1_freq={}
    s2_freq={}

    for i in range(len(s1)):
        s1_freq[s1[i]]=s1_freq.get(s1[i],0)+1
        s2_freq[s2[i]] = s2_freq.get(s2[i], 0) + 1

        if s1_freq==s2_freq:
            return True

    left=0
    for right in range(len(s1),len(s2)):
        s2_freq[s2[right]]=s2_freq.get(s2[right],0)+1
        s2_freq[s2[left]] -=1

        if s2_freq[s2[left]]==0:
            del s2_freq[s2[left]]

        left +=1

        if s1_freq==s2_freq:
            return True
    return False


s1 = "ab"
s2 = "eidboooo"
print(string_permutation(s1,s2))
