import pickle

D = {3: "Ample", 4: "Time"}
f = open("A1", "wb")
pickle.dump(D, f)
f.close()
f = open("A1", "rb")
data = pickle.load(f)
print(data)
