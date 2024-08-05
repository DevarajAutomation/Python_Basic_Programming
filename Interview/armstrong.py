def armstrong(n):
    s = n
    b = len(str(n))
    i_sum = 0

    while n != 0:
        r = n % 10
        i_sum = i_sum + (r ** b)
        n=n//10

    if s==i_sum:
        return True
    else:
        return False

n=153
print(armstrong(n))
