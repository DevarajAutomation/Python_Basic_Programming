fruits={'banana','apple','cherry','lemon','lemon'}
fruits.add("grape")

print('watermelon' in fruits)
print(fruits)
print(len(fruits))

fruits.update(['Mango','gauva'])
print(fruits)

vegetables={'potato','ladiesfinger','onion','lemon'}

veggies=fruits.intersection(vegetables)
print(veggies)

print(fruits.issubset(vegetables))
print(fruits.issuperset(vegetables))
