import re

with open("data.txt", "r") as fa:
    stra = fa.read()

pat = "\d+"

res = re.findall(pat, stra)

print(res)
