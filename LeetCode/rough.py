arr = [1,2,34,3,4,5,7,23,12]

lst=[]

for i in range(0,len(arr)-2,1):
    
    if arr[i] %2==1 and arr[i+1]%2==1  and arr[i+2] % 2 ==1:
        lst.append(arr[i])
        lst.append(arr[i+1])
        lst.append(arr[i+2])

print(lst)