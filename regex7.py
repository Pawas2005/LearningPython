# WAP to find first whitespace character in the string

import re

txt = "The rain in Spain"
x = re.search("\s", txt)
print(x)
print(x.start)
print(x.start())
