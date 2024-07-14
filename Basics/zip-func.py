fruits=['apple','mango','grape','banana']
vegetable=['carrot','ladies finger','bridal']

for f,v in zip(fruits,vegetable):
    print(f"fruit {f} and veggie {v}")


for f in enumerate(fruits):
    print(f)