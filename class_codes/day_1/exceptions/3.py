lista = [33, 76, 90, 12, 54, 67]

index = int(input("enter the index here: \n"))

try:
    print(lista[index])
except IndexError:
    print(f"{index} is wrong, defautling index value to 2")
    index = 2
    print(f"value is {lista[index]}")
