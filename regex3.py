# WAP to search any character except new line character where sequence
# starts with he followed by two characters N and O

import re

string = input()

x = re.findall("he..o", string)
print(x)
