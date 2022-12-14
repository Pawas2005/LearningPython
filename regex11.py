# WAP to find email from the text

import re

s = input("Enter string: ")
lst = re.findall(r"\S+@+\S+", s)
print(lst)
