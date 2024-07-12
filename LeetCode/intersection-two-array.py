"""https://leetcode.com/problems/intersection-of-two-arrays-ii/description/?envType=daily-question&envId=2024-07-02"""


def intersection_two_array(arr1,arr2):

    result=[]

    for i in arr1:
        if i in arr2:
            result.append(i)

    
    return result

    
nums1 = [4,9,5] 
nums2 = [9,4,9,8,4]
# nums1 = [1,2,2,1]
# nums2 = [2,2]
print(intersection_two_array(nums1,nums2))