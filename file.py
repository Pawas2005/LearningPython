# WAP to declare a dictionary and write that into file

L1 = input("Keys: ").split()
L2 = input("Values: ").split()

details = dict(zip(L1, L2))

with open('file.txt', 'w') as data:
    data.write(str(details))

with open('file.txt', 'r') as data2:
    data2.read()

