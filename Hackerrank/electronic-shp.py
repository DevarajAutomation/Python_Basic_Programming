"""https://www.hackerrank.com/challenges/electronics-shop/problem"""


def purchase_electronic(keyboards,drives,budget):

    money_spent=-1

    for keyboard in keyboards:
        for drive in drives:
            total_cost= keyboard + drive

            if total_cost <=budget and total_cost > money_spent:
                money_spent=total_cost
    return money_spent

b=60
key=[40,50,60]
dri=[5,8,12]

print(purchase_electronic(key,dri,b))