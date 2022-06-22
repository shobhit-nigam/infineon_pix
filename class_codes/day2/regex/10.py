import re

with open("data.txt", "r") as fa:
    stra = fa.read()

pat = "\d{3,}"
rep = "##"

strb = re.sub(pat, rep, stra, 3)

print(strb)
