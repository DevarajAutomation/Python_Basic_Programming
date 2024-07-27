def remove_duplicates(arr):
    result=[]

    for i in arr:
        if i not in result:
            result.append(i)

    return result

ar=[1, 1, 1, 2, 3, 3, 6, 6, 7]

print(remove_duplicates(ar))