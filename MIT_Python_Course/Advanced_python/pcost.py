
def calculcate_portfolio_cost(filepath):
    
    with open(filepath,'r') as f:
        
        total_sum=0.0
    
        for line in f:

            fields=line.split()
            try:
                shares=int(fields[1])
                price=float(fields[2])
                total_cost=total_sum+shares*price
            except ValueError("invalid literal for int() with base 10") as e:
                print(e)

            try:
                name=str(fields[0])
                price=float(fields[2])

                if  isinstance(name,str):
                    print(name)
                else:
                    print('No')

            except ValueError ('Name must be in string') as e:
                print(e)
            
            try:
                if "IBM" in name:
                    print('Yes')
            except ValueError as e:
                print(e)

            
        
calculcate_portfolio_cost("/workspaces/Python_Basic_Programming/Data/portfolio.dat")