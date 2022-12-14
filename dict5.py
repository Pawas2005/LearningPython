# WAP to take key and values inputs from user and create a dict
# Read a key from the user, if key is exist in dictionary, then remove the content otherwise print
# Key does not exist in dictionary

L1 = [int(x) for x in input("Enter the keys (Separated by comma): ").split(",")]
L2 = input("Enter the values (Separated by comma): ").split(",")
D1 = dict(zip(L1, L2))
print("Initial Squad", D1)
K = int(input("Enter key to delete: "))
if K in L1:
    D1.pop(K)
else:
    print("Key does not exist in dictionary")
print("Updated Squad:", D1)