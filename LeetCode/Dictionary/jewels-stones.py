
jewels = "aA"
stones = "aAAbbbb"

result={}

for i in range(len(stones)):
    if stones[i] in jewels:
        result[i]=stones[i]

print(result)
print(len(result))
