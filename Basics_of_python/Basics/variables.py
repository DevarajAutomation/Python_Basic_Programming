"""
cube=[(i**3) for i in range(1,5)]
print(cube)
"""

first_name='devaddevdaev'
last_name='Raja'

#print(first_name+last_name) #Concatenation
start='This is Deva'

"""Buit in Functions of String"""
# print(first_name.isalnum())
# print(first_name.capitalize())
# print(first_name.casefold())
# print(first_name.count(start))
# print(first_name.endswith(start))
# try:
#     print(last_name.index(start))
# except:
#     print('The given element/string not found')

#print("The \"Python\" \tEngineer- %s %s " %(start,last_name))

"""Print the area of cirle with radius 5 """

pi=3.142
r=5
area=pi * r*r
#print('The area of cirle is %.12f and it\'s radius is %d' %(area,r))

#print('The area of circle is {} and it\'s radius is {}'.format(area,r))

print(f"The area of circle is {area} and it\'s radius is {r}")