
""""""

def sparse_arrays(inpu, quer):
    results = []
    for i in range(len(quer)):
        if quer[i] in s:
            results.append(inpu.count(quer[i]))
        else:
            results.insert(i,0)

    return results


s = ['aba','baba','aba','xzxb']
q = ['aba','xzxb','ab']

print(sparse_arrays(s, q))
