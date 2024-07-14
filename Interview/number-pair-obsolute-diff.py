def absolute_difference(arr, k):
    result = []

    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            if abs(arr[i] - arr[j]) == k:
                result.append((i, j))

    return len(result)


nums = [1, 2, 2, 1]
k = 1

print(absolute_difference(nums,k))
