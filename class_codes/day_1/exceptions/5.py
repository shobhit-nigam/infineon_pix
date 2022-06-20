lista = [33, 76, 90, 12, 54, 67]


try:
    try:
        i = input("enter the index here: \n")
        index = int(i)
        print(lista[index])
    except ValueError:
        dicta = {"one":1, "zero":0, "three":3}
        if i in dicta:
            print(lista[dicta[i]])
        else:
            print("defaulting it to zero")
            print(lista[0])
except IndexError:
    print(f"{index} is wrong, defautling index value to 2")
    index = 2
    print(f"value is {lista[index]}")
except ValueError:
    print("value error exception is raised")
    print("defaulting the index to zero")
    index = 0
    print(f"value is {lista[index]}")
