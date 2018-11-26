import re

string = "Two aa too"

# m = re.findall("t[ow]o", string)
m = re.findall("t[ow]o", string, re.IGNORECASE)
print(m)


m = re.findall("t[^w]o", string, re.IGNORECASE)
print(m)