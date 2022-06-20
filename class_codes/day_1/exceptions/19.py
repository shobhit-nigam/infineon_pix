import traceback
import sys

#fa = open("error.log", "a")

lista = ["ww", "tt", "ff", "ss", "rr", 'ee']

try:
    i = int(input("enter a number:\n"))
    print(lista[i])
except:
    print("------")
    print(sys.exc_info())
    print("------")
print("xxx")
