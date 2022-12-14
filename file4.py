# WAP with try-except block, a and b as input

try:
    a = int(input("a: "))
    b = int(input("b: "))
    c = a + b
    d = a / b
    e = a * b
    print("try successful")
except ZeroDivisionError:
    print("Zero division error occurred")
except NameError:
    print("name error occurred")
except Exception:
    print("exception occurred")



