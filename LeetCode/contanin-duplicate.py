"""https://leetcode.com/problems/contains-duplicate/description/"""

def containsduplicate(arr):


  for i in arr:
        
            if arr.count(i) > 1:
                print(i)
                return True
       

            
nums = [2,14,18,22,22]



#print(containsduplicate(nums))