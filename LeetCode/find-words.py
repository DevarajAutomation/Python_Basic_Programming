"""https://leetcode.com/problems/find-words-containing-character/description/"""

def findwords(words,x):


    index_position=[(index) for index,element in enumerate(words) if x in element ]

    return index_position


words = ["abc","bcd","aaaa","cbc"]
x = "a"

print(findwords(words,x))