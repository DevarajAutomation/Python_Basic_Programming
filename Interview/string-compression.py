def compressed_string(strs):
    compressed_str = ""
    count = 1

    for i in range(len(strs) - 1):
        if strs[i] == strs[i + 1]:
            count += 1
        else:
            compressed_str += strs[i] + str(count)
            count = 1
    compressed_str += strs[i] + str(count)

    if len(compressed_str) >= len(strs):
        return strs
    else:
        return compressed_str

chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]

print(compressed_string(chars))
