# WAP to read user defined values and sort the contents of dictionary as per key
data1 = [int(x) for x in input().split(",")]
data2 = [int(y) for y in input().split(",")]
D1 = dict(zip(data1, data2))
for i in sorted(D1):
    print(i, D1[i])
