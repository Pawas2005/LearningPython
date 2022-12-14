#Program to make table of number
y="Y"
while y=="Y" or y=="y":
  N=float(input("Enter the number : "))
  for a in range(1,11):
    m=N*a
    print(N, "x", a, "is", m)
