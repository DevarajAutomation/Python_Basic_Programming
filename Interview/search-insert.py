def search_insert(arr,target):

    l=0
    r=len(arr)-1

    while l <= r:

        mid=(l+r)//2

        if target > arr[mid]:
            l=mid+1

        elif target < arr[mid]:
            r=mid-1
        else:
            return mid

    return l

nums = [1,3,5,6]
target = 5

print(search_insert(nums,target))
