def remove_element(arr,val):

    while val in arr:
        arr.remove(val)

    return arr

a=[3,2,2,3]
v=3
print(remove_element(a,v))