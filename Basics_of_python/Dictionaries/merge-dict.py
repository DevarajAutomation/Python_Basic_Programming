def merge_dictionary(dict1,dict2):

    merge={**dict1, **dict2}

    return merge


d1 = {1:"a", 2: "b"}
d2 = {3:"c", 4:"d"}

print(merge_dictionary(d1,d2))