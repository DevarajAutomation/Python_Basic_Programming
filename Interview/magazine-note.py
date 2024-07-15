from collections import Counter


def magazine_note(magazine, note):
    if Counter(note) - Counter(magazine) == {}:
        return 'Yes'
    else:
        return 'No'


m = "attack at dawn"
n= "Attack at dawn"

print(magazine_note(m,n))
