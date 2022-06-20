lista = [33, 76, 90, 12, 54, 67]
index = 0

def funca():
    global lista
    global index
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

try:
    funca()
except IndexError:
    print(f"{index} is wrong, defautling index value to 2")
    index = 2
    print(f"value is {lista[index]}")
