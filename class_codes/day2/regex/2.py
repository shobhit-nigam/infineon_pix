import re

with open("data.txt", "r") as fa:
    stra = fa.read()

pat = "\d+"

res = re.match(pat, stra)

if res:
    print("found it")
else:
    print("did not find it")
