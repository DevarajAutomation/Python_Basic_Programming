def reverse_array(arr):

    n=len(arr)
    count=0
    for i in range(n):
        for j in range(n-1):
            if arr[i] > arr[j]:
                arr[i],arr[j]=arr[j],arr[i]

    return arr


a=[1,2,3]
print(reverse_array(a))