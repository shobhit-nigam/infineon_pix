lista = [33, 76, 90, 12, 54, 67]
index = 0

try:
    i = input("enter the index here: \n")
    index = int(i)
    print(lista[index])
except Exception as obje:
    print("something went wrong, check below")
    print(obje)
