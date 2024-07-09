import csv
from pprint import pprint
from collections import defaultdict

file=open("/workspaces/Python_Basic_Programming/Data/portfolio.csv")

csv_reader=csv.reader(file)

header=next(csv_reader)

#print(header)

rows=list(csv_reader)
#print(rows)

# for row in rows:
#     pprint(row)


# for name,shares,price in rows:
#     print(name,shares,price)

# for name, _ , price in rows:
#     print(name,price)

"""use of default dictionaries"""

# byname=defaultdict(list)

# for name, *data in rows:
#     byname[name].append(data)
    

# print(byname['IBM'])
# print(byname['MSFT'])

"""Use enumurate function"""

# for index,row in enumerate(rows):
#     print(index,row)

"""use of zip function"""

row=rows[0]
print(row)

for col,val in zip(header,row):
    print(col,val)