def sub_array_sum(arr,k):
    seen={0:1}
    count=0
    s=0

    for i in arr:
        s+=i
        if (s-k) in seen:
            count +=1

        if s in seen:
            seen[s]+=1
        else:
            seen[s]=1

    return count

nums = [1,2,3]
k = 2
print(sub_array_sum(nums,k))