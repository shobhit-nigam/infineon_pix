import re
with open("numbers.txt", "r") as fa:
    stra = fa.read()

pat = r"(\d{5})-(\d{5})"

res = re.search(pat, stra)
if res:
    print("found it")

    print(res.groups())
    print(len(res.groups()))
    print(res.group(2))
