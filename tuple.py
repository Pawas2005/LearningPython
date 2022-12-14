n1 = int(input("Start Index: "))
n2 = int(input("End Index: "))
t = (10, 100, 50, 40, 30)
L = len(t)
if n1 > L or n2 > L+1:
    print("Index out of range")
else:
    res = t[n1:n2]
    print(res)
