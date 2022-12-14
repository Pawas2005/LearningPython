# WAP to create user defined exception class which is using arithmetic division operation
# Define a class our exception with exception as base class
# Use __init__ constructor with args (self, message)
# Define a new class using User Exception
# Start the try block and take a and b as input from the user
# If b=0 then raise our exception with msg that is b>0, otherwise do division

class OurException(Exception):
    def __init__(self, msg):
        self.msg = msg


class UsingOurException:
    try:
        a = int(input("a: "))
        b = int(input("b: "))
        if b == 0:
            raise OurException("b should be greater than zero")
        d = a / b
        print("Division successful with result:", d)
    except OurException as err:
        print("user defined exception:", err.msg)
