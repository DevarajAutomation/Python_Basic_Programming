s = "abcde"
t = "edbac"


result={}

for i in range(len(s)):
    if s[i] in t:
        diff = abs(i-t.index(s[i]))
        result[i]=diff

print(sum(result.values()))