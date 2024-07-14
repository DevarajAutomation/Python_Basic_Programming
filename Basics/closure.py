def summation():
    var=10
    def add(a=5):
        return a+var
    return add()

result=summation()
print(result)