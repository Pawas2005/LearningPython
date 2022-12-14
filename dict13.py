# WAP to create 2 dictioanaries.
# The first one has value of form - ordinal value, character from A-Z
# The first one has value of form - ordinal value, character from a-z
L1 = []
L2 = []
S = "QWERTYUIOPASDFGHJKLZXCVBNM"
for i in S:
    L1.append(i)
    L2.append(ord(i))
L1.sort()
L2.sort()
D1 = dict(zip(L2, L1))
D2 = dict(zip(L1, L2))
print(D1)
print(D2)
