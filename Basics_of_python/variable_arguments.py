def addition(*args):

    result=0

    for arg in args:
        result+=arg

    return result

print(addition(23,34,23,34))

my_list=[1,23,45,43,23]

print(addition(*my_list))