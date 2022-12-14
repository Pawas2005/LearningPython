d1 = {"RegNo": [1234, 1111, 1115], "Name": ["Rohit", "Arjun", "Rahul"]}
print(d1)
print(d1["RegNo"])
print(d1["RegNo"][1])
d2 = {("65", "K22SH"): "Sky", ("65", "K22HH"): "Abhinav"}
print(d2["65", "K22SH"])
for i, j in d2:
    print(d2[i, j])
