import traceback

fa = open("error.log", "a")

lista = ["ww", "tt", "ff", "ss", "rr", 'ee']

try:
    i = int(input("enter a number:\n"))
    print(lista[i])
except:
    print("------")
    traceback.print_exc(file=fa)
    print("------")
close(fa)
print("xxx")
