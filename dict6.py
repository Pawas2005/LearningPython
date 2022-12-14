# WAP to create a dictionary using two lists
# Create the two lists using user given elements
# If the size of both lists is different, then print "Length should be equal"
# Otherwise prepare dictionary from it
L1 = [int(x) for x in input().split(',')]
L2 = input().split(",")
if len(L1) == len(L2):
    D1 = dict(zip(L1, L2))
    print(D1)
else:
    print("Length should be equal")

