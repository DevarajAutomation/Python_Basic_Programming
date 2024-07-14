def rotate_array(arr, d):
    n = len(arr)

    arr[:] = arr[d:n] + arr[0:d]
    return arr


x = [1, 2, 3, 4, 5, 6, 7, 8]
print(rotate_array(x,1))
