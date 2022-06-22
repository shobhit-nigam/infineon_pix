import re
with open("numbers.txt", "r") as fa:
    stra = fa.read()

pat = "\d{5}-\d{5}"
#phone_num_re

print(re.findall(pat, stra))
