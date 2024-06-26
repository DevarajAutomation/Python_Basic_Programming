"""https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/description/"""

def canBeIncreasing(num):
    def stictly_increase(arr):

        return all(arr[i] < arr[i+1] for i in range(len(arr)-1))
    
    for i in range(len(num)-1):
        if num[i] >= num[i+1]:
            if stictly_increase(num[:i] + num[i+1:]):
                return True
            if stictly_increase(num[:i+1]+ num[i+2:]):
                return True
            
        
            return False
        
    return True


arr=[1,1,1]
print(canBeIncreasing(arr))