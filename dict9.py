# WAP to traverse a dictionary as per the case mentioned here

d1 = {("65", "K22SH"): [80, 40, 60], ("65", "K22HH"): [40, 85, 35], ("63", "K22SH"): [20, 20, 40]}
for i, j in d1:
    print(j, i, sep="", end=" ")
    print(d1[i, j][1])
