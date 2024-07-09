import collections
import collections.abc

class ReadData(collections.abc.Sequence):

    def __init__(self):
        self.route=[]
        self.date=[]
        self.daytype=[]
        self.rides=[]
    def __len__(self):
        return len(self.route)
    
    def __getitem__(self,index):

        return {
            'route':self.route[index],
            'date':self.date[index],
            'daytype':self.daytype[index],
            'ride':self.rides[index]

        }
    def append(self,d):
        self.route.append(d['route'])
        self.date.append(d['date'])
        self.daytype.append(d['daytype'])
        self.rides.append(d['ride'])

records=ReadData()

print(records.append())