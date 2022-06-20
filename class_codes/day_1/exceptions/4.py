lista = [33, 76, 90, 12, 54, 67]


try:
    index = int(input("enter the index here: \n"))
    print(lista[index])
except IndexError:
    print(f"{index} is wrong, defautling index value to 2")
    index = 2
    print(f"value is {lista[index]}")
except ValueError:
    print("value error exception is raised")
    print("defaulting the index to zero")
    index = 0
    print(f"value is {lista[index]}")
