def find_element(arr,k):

    arr.sort()

    for i in range(len(arr)):
        return arr[k-1]


ar=[7, 10, 4, 3, 20, 15]
k=4
print(find_element(ar,k))
