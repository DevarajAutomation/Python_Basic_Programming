"""https://leetcode.com/problems/contains-duplicate/description/"""

def contains_duplicate(nums):
    nums_set=set()

    for i in nums:
        if i in nums_set:
            return True
        else:
            nums_set.add(i)
    return False

nums = [1,1,1,3,3,4,3,2,4,2]

print(contains_duplicate(nums))