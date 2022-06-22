import re

with open("data.txt", "r") as fa:
    stra = fa.read()

pat = "\d+"

res = re.split(pat, stra)
print(res)
