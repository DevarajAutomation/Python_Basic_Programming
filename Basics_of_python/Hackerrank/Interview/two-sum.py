"""https://leetcode.com/problems/two-sum/description/"""

def two_sum(arr,target):

    # seen={}

    # for i in range(len(arr)):
    #     diff=target-arr[i]
    #     if diff in seen:   
    #         return [seen[i],i]
    #     else:
    #         seen[arr[i]]=i  #2:0

    for i in range(len(nums)):
        for j in range(1,len(nums)):
            if nums[i] + nums[j]==target:
                return [i,j]
nums = [2,7,11,15]
tar=9
print(two_sum(nums,tar))