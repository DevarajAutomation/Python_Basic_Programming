def union_two_arrays(arr1, arr2):
    s1 = set(arr1)
    s2 = set(arr2)

    result = list(s1.union(s2))

    return result


arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
print(union_two_arrays(arr1, arr2))
