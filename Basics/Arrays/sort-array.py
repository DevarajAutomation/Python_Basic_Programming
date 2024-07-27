def sort_array(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    right = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    left = [x for x in arr if x > pivot]

    return sort_array(right) + sort_array(mid) + sort_array(left)

a=[2,1,4,3]
print(sort_array(a))
