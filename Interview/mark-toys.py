def mark_toys(prices,k):

    count=0
    sum=0

    for i in prices:
        sum+=i
        if sum > k:
            break

        else:
            count +=1

    return count

p=[1,2,3,4]
k=7
print(mark_toys(p,k))