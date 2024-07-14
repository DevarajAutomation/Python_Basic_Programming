

test_str = 'Gfg is best'

res={key:test_str.count(key) for key in test_str.split()}

print(res)