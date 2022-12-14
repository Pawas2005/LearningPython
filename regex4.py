

import re

txt = input()

x = re.findall("^hello", txt)

if x:
    print("Yes, the string starts with 'hello'")
else:
    print("No match")