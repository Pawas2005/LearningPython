# WAP to create a dictionary, make use of open function to open a file in binary mode
# Make use of pickle.dump to write data stream into file
# Make use of pickle.load to load the data stream from file onto console

import pickle

L1 = input("Keys: ").split()
L2 = [int(x) for x in input("Values: ").split()]
D = dict(zip(L1, L2))
outfile = open("animals", "wb")
pickle.dump(D, outfile)
outfile.close()
fst = open("animals", "rb")
data = pickle.load(fst)
try:
    while True:
        print(data)
        data = pickle.load(fst)
except:
    print("Bye")
