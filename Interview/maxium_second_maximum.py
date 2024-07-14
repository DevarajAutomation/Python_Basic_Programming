def maximum_second_maximum(arr):

    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
                
    return arr[-1],arr[-2]

nums=[2, 3, 4, 5, 6, 7, 8, 1]
print(maximum_second_maximum(nums))
