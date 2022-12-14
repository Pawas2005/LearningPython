keys = [x for x in input("Enter Keys: ").split(",")]
values = [y for y in input("Enter Values").split(",")]
D1 = dict(zip(keys, values))
D3 = {}
print(D1)
for key in D1:
    D3[D1[key]] = key
print(D3)
