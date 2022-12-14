count = 0
s = input("Data: ")
char = int(input("Element to count: "))
L = s.split(",")
for x in range(len(L)):
    L[x]=int(L[x])
t = tuple(L)
for i in t:
    if char in i:
        count += 1
if count > 0:
    print("Number of occurrences:", count)
else:
    print("Not in Tuple")
