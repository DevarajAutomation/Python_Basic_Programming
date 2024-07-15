def pair_socks(arr):

    pairs_socks=[0 for i in range(101)]

    for element in arr:
        pairs_socks[element]=pairs_socks[element]+1

    ans=0

    for socks in pairs_socks:
        ans+=socks//2
    return ans

a=[1,2,1,2,1,3,2]
print(pair_socks(a))