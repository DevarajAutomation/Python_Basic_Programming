"""https://leetcode.com/problems/search-insert-position/description/"""

def search_insert(nums,target):

    l=0
    r=len(nums)-1

    while l <= r:
        mid=(l+r)//2

        if target > nums[mid]:
            l=mid+1
        elif target < nums[mid]:
            r=mid-1
        else:
            return mid
    return l

nums = [1,3,5,6]
target = 7

print(search_insert(nums,target))