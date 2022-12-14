# WAP to combine contents of two dictionaries into a third dictionary with copy

d1 = {"RegNo": [1234, 1111, 1115], "Name": ["Rohit", "Arjun", "Rahul"]}
d2 = {("65", "K22SH"): "Sky", ("65", "K22HH"): "Abhinav"}
d3 = d1.copy()
d3.update(d2)
print(d3)
