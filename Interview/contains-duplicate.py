def contains_duplicate(arr):

    nums_set=set()

    for i in arr:
        if i in nums_set:
            return True
        else:
            nums_set.add(i)

    return False

nums = [1,2,3,4]

print(contains_duplicate(nums))
