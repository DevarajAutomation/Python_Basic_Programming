import sys

arr=[]

# print(sys.getsizeof(arr))
# arr.append(3)
# print(sys.getsizeof(arr))
# arr.append(5)
# print(sys.getsizeof(arr))
# arr.append(4)
# print(sys.getsizeof(arr))
# arr.append(9)
# print(sys.getsizeof(arr))
# arr.append(2)
# print(sys.getsizeof(arr))
# arr.append(4)
# print(sys.getsizeof(arr))

row = { 'route': '22', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354 }

print(sys.getsizeof(row))

row['a']=1
print(sys.getsizeof(row))
row['apple']=4
print(sys.getsizeof(row))
row['mysore']=9
print(sys.getsizeof(row))
del row['mysore']
print(sys.getsizeof(row))
print(row)
del row['apple']
print(sys.getsizeof(row))
del row['a']
print(sys.getsizeof(row))