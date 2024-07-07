class Stock:

    def __init__(self,filepath):
        self.filepath=filepath

    def calculate_cost(self):
        

        with open(self.filepath ,'r') as file:
            
            total_sum=0.0

            for line in file:
                fields= line.split()
                shares=int(fields[1])
                price=float(fields[2])

            return total_sum+ shares * price
        
s1=Stock("/workspaces/Python_Basic_Programming/Data/portfolio.dat")

print(s1.calculate_cost())


    