def bubble_sort(arr):
    n=len(arr)
    count=0
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1]= arr[j+1],arr[j]
                count+=1
    print("Array is sorted in {} swaps".format(count))
    print("First element {}".format(arr[0]))
    print("Last element {}".format(arr[-1]))

a = [33,2,5,1,7,9,4]
bubble_sort(a)


