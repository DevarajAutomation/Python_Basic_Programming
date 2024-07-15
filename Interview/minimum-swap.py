"""https://www.hackerrank.com/challenges/minimum-swaps-2/problem"""

def minimum_swaps(arr):

    i=0
    count=0
    while i < len(arr):
        if arr[i] !=i+1:

            arr[arr[i]-1],arr[i]=arr[i],arr[arr[i]-1]

            count +=1

        else:
            i+=1

    return arr

arr=[7, 1, 3, 2, 4, 5, 6]

print(minimum_swaps(arr))