class Sqaure:

    info="Hi, I am square! find my area"

    def __init__(self):
        pass
        
    def area(self,length,breadth):
        self.length= int(length)
        self.breadth=int(breadth)
        return self.length * self.breadth
        
    

sq1=Sqaure()
sq2=Sqaure()
print(sq1.area(3,4))