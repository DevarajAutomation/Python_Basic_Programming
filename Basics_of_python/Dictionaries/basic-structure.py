iternary = {"Chennai": "Bangalore",
            "Bombay":"Delhi",
            "Goa":"Chennai",
            "Delhi": "Goa"}

origin=''
for i in iternary.keys():
    if i not in iternary.values():
        origin=i

destination_1=iternary[origin]
destination_2=iternary[destination_1]
destination_3=iternary[destination_2]
destination_4=iternary[destination_3]
new_iternary={}

new_iternary[origin]= destination_1
new_iternary[destination_1]=destination_2
new_iternary[destination_2]=destination_3
new_iternary[destination_3]=destination_4
#print(sorted(new_iternary.items()))