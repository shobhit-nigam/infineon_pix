lista = [33, 76, 90, 12, 54, 67]
index = 0

try:
    i = input("enter the index here: \n")
    index = int(i)
    print(listb[index])
except ValueError:
    dicta = {"one":1, "zero":0, "three":3}
    if i in dicta:
        print(lista[dicta[i]])
    else:
        print("defaulting it to zero")
        print(lista[0])
except:
    print("all exceptions handled here, code wont stop executing")
