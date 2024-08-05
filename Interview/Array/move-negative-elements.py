def move_negative_elements(arr):
    n=len(arr)
    j=0

    for i in range(0,n):
        if arr[i] < 0:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            j+=1

    return arr[::-1]

arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
print(move_negative_elements(arr))