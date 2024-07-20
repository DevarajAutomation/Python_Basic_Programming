def merge_string_alternative(s1, s2):
    result = []

    for w1, w2 in zip(s1, s2):
        result.append(w1 + w2)

    result.append(s1[len(s2):])
    result.append(s2[len(s1):])

    return "".join(result)


a = 'abc'
b = 'dcg'

print(merge_string_alternative(a, b))
