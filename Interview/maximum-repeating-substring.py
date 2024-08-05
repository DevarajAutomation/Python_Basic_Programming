
def maximum_repeating_sub_string(seq ,word):
    res =0
    if word in seq:
        res += seq.count(word)

        return res
    else:
        return 0

sequence = "ababc"
word = "ab"

print(maximum_repeating_sub_string(sequence,word))