# if an element in the list, then remove that element, otherwise mention that does not exist in the list
# read an element details from the user

L = [1000, 87, 85, 35, 95]
print(L)
a = int(input("Enter element to remove: "))
if a in L:
    L.remove(a)
    print(L)
else:
    print("Does not exist in list")
