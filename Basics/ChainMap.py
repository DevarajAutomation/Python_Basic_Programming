from collections import ChainMap

d1={'a':1,'b':2}
d2={'b':2,'c':3}
d3={'a':3,'d':5}

d4={'c':4,"d":5}
data=ChainMap(d1,d2,d3)

data1=data.new_child(d4)

print(data1)