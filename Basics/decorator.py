

def make_square(function):
    def wrapper():
        func=function()
        make=func.upper()
        return make
    return wrapper

@make_square
def addition():
    return 'hello'

print(addition())