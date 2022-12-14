# Wap to update the list L1=[1, 4, 5, 6, 7] read value and index from user.
# If index is in range then update the list otherwise show index is out of range

a = 'Y'
while a == "y" or a == "Y":
    L = [1, 4, 5, 6, 7]
    print("L = [1, 4, 5, 6, 7]")
    value = int(input("Enter new value: "))
    index = int(input("Enter the index: "))
    if 0 < index < len(L):
        L[index] = value
        print("Updated List =", L)
    else:
        print("Out of range")
    a = input("Do you want to perform another update (y/n): ")
