# Create two dictionaries with user given key and value pairs
# Print the dict 1 in sorted order
# Create a copy of dictionary and print keys and values in sorted order
# Update the sorted dictionary 1 with dictionary 2

data1 = [int(x) for x in input("Keys for dict 1: ").split(",")]
data2 = [int(y) for y in input("Values for dict 2: ").split(",")]
data3 = [int(x) for x in input("Keys for dict 3: ").split(",")]
data4 = [int(y) for y in input("Values for dict 4: ").split(",")]
dict1 = dict(zip(data1, data2))
dict2 = dict(zip(data3, data4))
L1 = []
L2 = []
for i in sorted(dict1):
    L1.append(i)
    L2.append(dict1[i])
dict1 = dict(zip(L1, L2))
print(dict1)
dict3 = dict1.copy()
print(dict3)
dict1.update(dict2)
print(dict1)


