def single_number(arr):
    n = len(arr)

    for i in range(n):
        if arr.count(arr[i]) == 1:
            return arr[i]

ar=[1]
print(single_number(ar))