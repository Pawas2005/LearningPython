k=input("Enter String")
"""
sample input : cold
expected output : ccoolldd
"""
n=int(input("Number of repetition"))
print("".join([char*n for char in k]))