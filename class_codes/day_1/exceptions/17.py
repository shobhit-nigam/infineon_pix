import traceback

lista = ["ww", "tt", "ff", "ss", "rr", 'ee']

try:
    i = int(input("enter a number:\n"))
    print(lista[i])
except:
    print("------")
    traceback.print_exc()
    print("------")

print("xxx")
