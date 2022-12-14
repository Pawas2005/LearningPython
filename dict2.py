x = int(input("Enter number of entries: "))
L = []
for i in range(x):
    data = input("Enter name and registration number (Separated by ',' )")
    l1 = data.split(",")
    t1 = tuple(l1)
    L.append(t1)
D = dict(L)
print(D)
