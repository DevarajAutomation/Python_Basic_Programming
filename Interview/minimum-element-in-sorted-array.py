def minimum_element_in_sorted_array(arr):
    n=len(arr)
    count=0

    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                count +=1

    return arr[1]

ar=[5, 6, 1, 2, 3, 4]
print(minimum_element_in_sorted_array(ar))