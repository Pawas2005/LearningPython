a="y"

while a=="y":
    n = int(input("Enter the Number"))
    if n>1:
        while n>1:
            n=n-1
            f=n*(n+1)
            print(f)
    elif n==1:
        print(1)
    elif n==0:
        print(1)
    else:
        print("Invalid Input")