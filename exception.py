# WAP to define a function check age with parameter age.
# Check if the age is less than zero, raise an exception ValueError if it's true
# the function check it and start the try block
# Ask user to input age and call checkit function
# The except block handles a value error by printing to console that
# age should be greater than or equal to zero
# also include finally block

def checkage(a):
    if a < 0:
        raise ValueError("age should be greater than or equal to zero")
    print("age is valid")


try:
    age = int(input("age: "))
    checkage(age)
except ValueError as err:
    print(err.args)
finally:
    print("executed in any condition")
