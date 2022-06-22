import re

with open("data_2.txt", "r") as fa:
    stra = fa.read()

pat = "re"

strb = re.findall(pat, stra, re.IGNORECASE)

print(strb)
