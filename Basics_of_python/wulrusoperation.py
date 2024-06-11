""" Let say we have to take input from the user and compare with the strings"""


# while (thestr := input('Value?')) != "exit":
#     print(thestr)
#     thestr = input('Value?')

data_point= [12,13,14]

data_results={
    'size' : ( l:= len(data_point)),
    'total' : (s:= sum(data_point)),
    'avg'  : s/l
}

print(data_results)