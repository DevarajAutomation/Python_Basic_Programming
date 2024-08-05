def reverse_string(word,ch):

    if ch not in word:
        return word
    else:
        index = word.index(ch)

        res = ""
        for i in reversed(range(0, index+1)):
            res += word[i]

        return res+word[index+1:]

word ="xyxzxe"
ch = "z"
print(reverse_string(word,ch))

