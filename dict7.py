# WAP to find minimum and maximum value from the dict
L1 = [int(x) for x in input("Enter Keys: ").split(",")]
L2 = [int(y) for y in input("Enter Values").split(",")]
D1 = dict(zip(L1, L2))
print(D1)
mi = L2[0]
ma = L2[0]
mi2 = L1[0]
ma2 = L1[-1]
for j in L2:
    if j < mi2:
        mi = j
    if j > ma2:
        ma = j
for i in L2:
    if i < mi:
        mi = i
    if i > ma:
        ma = i
print("Maximum Value:", ma)
print("Minimum Value:", mi)
print("Maximum Key:", ma2)
print("Minimum Key:", mi2)
