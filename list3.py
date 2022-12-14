def insert(value, index):
    L.insert(value, index)
    print("Updated List =", L)


def remove(value):
    L.remove(value)
    print("Updated List =", L)


L = ["Apple", "Mango", "Orange"]
print("1. Insert")
print("2. Remove")
x=int(input("Choose Operation (1 or 2)"))
if x==1:
    v=int(input())
    i=int(input())
    insert(v, i)
elif x==2:
    v=int(input())
    remove(v)

