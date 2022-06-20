import traceback
import sys

#fa = open("error.log", "a")

lista = ["ww", "tt", "ff", "ss", "rr", 'ee']

try:
    i = int(input("enter a number:\n"))
    print(lista[i])
except Exception as obje:
    print("------")
    list_err = traceback.format_exception(type(obje), value=obje, tb=obje.__traceback__)
    print(list_err[2])
    print("------")
print("xxx")
