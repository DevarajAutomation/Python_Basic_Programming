def rich_customer(accounts):

    customers=[]
    for money in accounts:
        customers.append(sum(money))

    return max(customers)

accounts = [[2,8,7],[7,1,3],[1,9,5]]
print(rich_customer(accounts))