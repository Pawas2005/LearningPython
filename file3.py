# Take 2 integer inputs num1 and num2 from the user using input() function.
# Divide num1 and num2 using try-except block.
# Print results as shown in examples.


try:
    num1 = int(input())
    num2 = int(input())
except:
    print("Please input integer")

try:
    print(num1/num2)
except:
    print("Exception occurred")
