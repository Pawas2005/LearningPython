import re

txt = "The rain in Spain"

x = re.sub("\s", "g", txt)

print(x)
