# Wap to declare two list l1 and l2 then add L2 contents into L1 as individual elements.

L1 = ['Happy', 'Rohit', 'gemini']
L2 = [1, 2, 3]
for a in L2:
    L1.append(a)
# L1.extend(L2)
print(L1)
