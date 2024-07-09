arr=[1,2,3,4,5]

#squares=(x**2  for x in arr )

# print (squares)

# print(next(squares))
# print(next(squares))
# print(next(squares))
# print(next(squares))
# for i in squares:
#     print(i)

# for n in squares:
#     print(n)

def squares(arr):
    for n in arr:
        yield n * n


for x in squares(arr):
    print(x)