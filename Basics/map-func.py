nums=[1,2,3,4,5]

def squares(x):
    return x**2

squared_num=map(squares,nums)

print(list(squared_num))