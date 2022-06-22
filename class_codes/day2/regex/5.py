import re

with open("data.txt", "r") as fa:
    lista = fa.readlines()

pat = "\d{3,}"

for i in range(len(lista)):
    res = re.findall(pat, lista[i])
    if res:
        print(f"at line {i+1} we found {res}")
