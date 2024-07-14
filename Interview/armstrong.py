def armstrong(n):

    s=n
    b=len(str(n))

    sum=0

    while n !=0:
        r=n%10
        sum=sum+(r**b)
        n=n//10

    if sum==s:
        print(True)
    else:
        print(False)

n=153
x = 1253
armstrong(n)
armstrong(x)