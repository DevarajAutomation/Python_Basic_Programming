import re


file="C:/Users/devaraju.th/PycharmProjects/Bytes/Basics/data.txt"

file_read=open(file,'r')
f=file_read
pattern='devices'
replace_word='Nodes'
match=re.findall(pattern,f,re.I)
print(match.count(pattern))

replace=re.sub(pattern,replace_word,f,re.I)

re_match=re.findall(replace_word,f,re.I)
