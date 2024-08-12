def rotate_array_2(arr, k):
    n = len(arr)
    k = k % n
    rotated = [0] * n

    for i in range(n):
        rotated[(i + k) % n] == arr[i]

    for i in range(n):
        arr[i] = rotated[i]

    return rotated


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate_array_2(nums, k))
