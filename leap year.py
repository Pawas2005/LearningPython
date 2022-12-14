#WAP to  read year from user, and check whether that year is leap or not
a='y'
while a=="y":
    year=int(input("Enter Year: "))
    if year%400==0:
        print("Leap Year")
    elif year%100==0:
        print("Not a Leap Year")
    elif year%4==0:
        print("Leap Year")
    else:
        print("Not a Leap Year")