def maximum_element(arr):

   arr.sort()
   return arr[-1]


ar=[10, 20, 15, 2, 23, 90, 67]
print(maximum_element(ar))