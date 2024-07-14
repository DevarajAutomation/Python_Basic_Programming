"""https://leetcode.com/problems/valid-anagram/submissions/1319423930/"""


def valid_anagram_check(s, t):
    s_freq = {}
    t_freq = {}

    for char in s:
        s_freq[char] = s_freq.get(char, 0) + 1

    for char in t:
        t_freq[char] = t_freq.get(char, 0) + 1

    return s_freq == t_freq


s = "anagram"
t = "nagaram"

print(valid_anagram_check(s,t))
