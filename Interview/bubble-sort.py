def bubble_sort(arr):
    n = len(arr)
    count = 0

    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                count += 1

    return arr


a = [33, 2, 5, 1, 7, 9, 4]
print(bubble_sort(a))
