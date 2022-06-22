import re

with open("marvel.txt", "r") as fa:
    stra = fa.read()

pat = "-"

res = re.split(pat, stra)
print(res)

print(stra.split("-"))
