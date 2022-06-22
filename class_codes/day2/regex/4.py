import re

with open("data.txt", "r") as fa:
    stra = fa.read()

pat = "\d{3,}"

res = re.findall(pat, stra)

print(res)
