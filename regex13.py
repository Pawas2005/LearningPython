# WAP to find match group in regular expression

import re

s = input()
matchObj = re.match(r"(.*) are (.*?) .*", s)
print("matchObj.group() :", matchObj.group())
print("matchObj.group() :", matchObj.group())
print("matchObj.group() :", matchObj.group())
