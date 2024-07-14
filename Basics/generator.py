def generate_nums():
    yield 1
    yield 2
    yield 3
    yield 4


for v in generate_nums():
    print(v)
