# to remove duplicate elements from list

L1 = [10, 20, 10, 30]
L2 = []
for a in range(len(L1)):
    if L1[a] not in L2:
        L2.append(L1[a])
print(L1)
print(L2)
