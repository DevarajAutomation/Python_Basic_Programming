
print("before")


try:
    #4/0
    print(name)
except NameError as e:
    print('something is wrong')
    print(e)
except:
    print('we cannot divide by zero')

print('after')

def get_name(name):

    if len(name) <= 0:
        raise Exception ("The name can't be empty")
    

name=input('Enter the name')
get_name(name)


