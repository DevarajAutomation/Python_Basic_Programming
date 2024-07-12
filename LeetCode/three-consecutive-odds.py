"""https://leetcode.com/problems/three-consecutive-odds/description/?envType=daily-question&envId=2024-07-01"""

def consective_three(arr):

    if len(arr) < 3:
        return False
    result=[]
    
    for i in range(len(arr)-2):
        if arr[i] %2 ==1 and arr[i+1]%2==1 and arr[i+2]%2==1:
            result.append(arr[i])
            result.append(arr[i+1])
            result.append(arr[i+2])

        if len(result) >=3:
            return True
    return False

#arr = [1,2,34,3,4,5,7,23,12]
arr = [2,6,4,1]

print(consective_three(arr))










