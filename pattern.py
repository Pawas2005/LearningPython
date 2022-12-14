# WAP to print pattern
"""
n = int(input())
for i in range(n + 1):
    print("*" * i)
"""

# This is the correct program, to get a space after each *
"""
n = int(input())
for i in range(1, n+1):
    for j in range(i):
        print("*", end=" ")
    print("\n") # Inserts a new line
"""

# to print numbers
"""
n = int(input("Enter Number: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print("")


# reversing the upper pattern

n = int(input("Enter Number: "))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j, end=" ")
    print("")
"""
# For Alphabet Pattern

n = int(input("Enter Number"))
a = 65
for i in range(n):
    for j in range(i+1):
        print(chr(a + j), end=" ")
    print()
