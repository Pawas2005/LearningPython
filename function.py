# Call a function using fact(a) of a number


a = int(input("Enter Number"))


def fact(n):
    f = 1  # Using for loop
    for i in range(n, 0, -1):
        f *= i
    print(f)

    fac = 1  # Using while loop
    while n != 0:
        fac *= n
        n -= 1
    print(fac)


fact(a)
