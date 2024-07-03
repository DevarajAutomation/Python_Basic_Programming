# def sub_string(s):

#     start,max_len,max_sub_string=0,0,""
#     used_char={}
#     for i in range(len(s)):
#         if s[i] in used_char and start <=used_char[s[i]]:
#             start=used_char[s[i]]+1

#         else:
#             if i-start+1 > max_len:
#                 max_len=i-start+1
#                 max_sub_string= s[start:i+1]

#         used_char[s[i]]=i

#     return max_sub_string
    



sub="abcabcbb"

# print(sub_string(sub))

for i in range(len(sub)):
 print(sub[i])


