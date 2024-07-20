def print_duplicates(arr):
    n_freq={}
    result=[]

    for i in arr:
        n_freq[i]=n_freq.get(i,0)+1

    for k,v in n_freq.items():
        if v > 1:
            result.append(k)

    if not result:
        return -1

    return result

ar=[1, 2, 3, 6, 3, 6, 1]
print(print_duplicates(ar))