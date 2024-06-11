from string import Template


str1='Github'
str2='Dev'
output=f"{str2} works in {str1}"
print(output)

temp1=Template("${author} works in ${title}")

str3=temp1.substitute(author='Dev',title='Github')

print(str3)