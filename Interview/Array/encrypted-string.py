def encrypted_string(test_str, k):
    result = ""
    n = len(test_str)

    for i in range(n):
        j = (i + k)
        if j >= n:
            j = j % n
        result += test_str[j]

    return result


t = "dart"
k = 3

print(encrypted_string(t, k))
