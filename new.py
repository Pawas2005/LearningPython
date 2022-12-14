#This is a python program
"""It finds powers of numbers
It reruns itself with confirmation"""
y_or_n ="y"

while y_or_n == 'y':
    k=int(input("Enter number : "))
    j=int(input("Enter power : "))
    c=k**j
    print(k, "raised to the power", j, "is", c)
    y_or_n = input("Do you want to find another power or not? y/n: ")