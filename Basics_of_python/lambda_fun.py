"""Lambda functions are small ananymous functions which accepts the parameters and produces ouput in a single line"""

# lambda <input variabe> : <parameter> <expression>

def celsius_to_fahrenheit(temp):

    return (temp * 9/5) + 32

def fahrenheit_to_celsius(temp):
    return (temp-32) * 5/9

ctemp=[24,34,21,45,35]
ftemp=[98,99,89,90]
#lambda function
print(list( map(lambda t: (t * 9/5) + 32,ctemp)))
print(list( map(lambda t: (t -32 ) * 5/9,ftemp)))
# print(list(map(celsius_to_fahrenheit,ctemp)))
# print(list(map(fahrenheit_to_celsius,ftemp)))