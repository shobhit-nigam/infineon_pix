import re

stra = input()

pat = "^hell"

res = re.match(pat, stra)

if res:
    print("found it")
else:
    print("did not find it")
