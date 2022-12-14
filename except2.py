# WAP to open a file KK1.txt in read mode
# If file does not exist, throw an exception

try:
    open("KK1.txt", "r")
except FileNotFoundError:
    print("File does not exist")
