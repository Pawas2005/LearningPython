# WAP with a try block and two except blocks that handles two types of exceptions

r = "y"
while r == "y" or r == "Y":
    try:
        a = int(input("a: "))
        b = int(input("b: "))
        c = a + b
        d = a / b
        e = a * b
        print("try successful")
    except ZeroDivisionError:
        print("Zero division error occurred")
    except ArithmeticError:
        print("arithmetic error occurred")
    except Exception:
        print("exception occurred")
    finally:
        r = input("Do you want to run another program ? (Y/N) ")
