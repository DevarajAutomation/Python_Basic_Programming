def armstrong(n):

    s=n
    b=len(str(n))
    summ=0

    while n!=0:
        r=n%10
        summ=summ+(r**b)
        n=n//10

    if summ==s:
        return  True
    else:
        return False

n=154

print(armstrong(n))