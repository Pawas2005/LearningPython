# WAP to find Fibonacci Series upto n terms

n = int(input("Enter number of terms : "))
n1 = 0
n2 = 1
print(n1)
print(n2)
for i in range(n - 2):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(n3)
