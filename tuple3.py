s = input("Data: ")
l1 = s.split(" ")
for a in range(len(l1)):
    l1[a] = int(l1[a])
t1 = tuple(l1)
print(t1)
res = sum(t1)
print(res)
