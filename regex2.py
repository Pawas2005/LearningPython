# WAP tp find characters from string which os not containing a to c

import re

s = input()
x = re.findall("[^a-c]", s)
print(*x)
