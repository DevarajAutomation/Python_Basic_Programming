"""https://www.hackerrank.com/challenges/sock-merchant/problem"""



def sales_by_match(ar):
    list_of_socks=[0 for i in range(101)]

    for ele in ar:
        list_of_socks[ele]=list_of_socks[ele] + 1

    ans=0

    for sock in list_of_socks:
        ans+= sock//2

    return ans

ar=[1,2,1,2,1,3,2]

print(sales_by_match(ar))