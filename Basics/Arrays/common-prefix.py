def longest_common_prefix(arr):
    base_word = arr[0]

    for i in range(len(base_word)):
        for word in arr:
            if i == word[i] or word[i] != base_word[i]:
                return base_word[0:i]


ar = ["flower", "flow", "float"]

print(longest_common_prefix(ar))
