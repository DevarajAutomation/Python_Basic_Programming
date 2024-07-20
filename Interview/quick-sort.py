def quick_sort(arr):
    if len(arr) <=1:
        return arr

    pivot= arr[len(arr)//2]

    left=[x for x in arr if x < pivot]
    middle = [x for x in arr if x==pivot]
    right=[x for x in arr if x > pivot]

    return quick_sort(left) + quick_sort(middle) + quick_sort(right)

arr = [7, 2, 1, 6, 8, 5, 3, 4]

print(quick_sort(arr))

