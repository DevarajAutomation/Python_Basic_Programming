import csv

import tracemalloc
def read_rides_as_coloumns(filepath):

    routes=[]
    date=[]
    daytype=[]
    rides=[]
    tracemalloc.start()

    with open(filepath,'r') as file:
        csv_reader=csv.reader(file)

        header=next(csv_reader)

        for row in csv_reader:
            routes.append(row[0])
            date.append(row[1])
            daytype.append(row[2])
            rides.append(row[3])

    return dict(route=routes,date=date,daytype=daytype,rides=rides)

print(read_rides_as_coloumns("/workspaces/Python_Basic_Programming/Data/cts.csv"))
