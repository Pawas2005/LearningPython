# WAP to transverse a matrix
L = []

M = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
for i in range(len(M) + 1):
    L1 = []
    for j in M:
        L1.append(j[i])
    L.append(L1)
print(L)
