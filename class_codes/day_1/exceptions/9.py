lista = [33, 76, 90, 12, 54, 67]
index = 0

try:
    index = int(input("enter the index here: \n"))
    print(lista[index])
except IndexError:
    print("index is out of bound")
    print("default to zero, lista[index] =", lista[0])
else:
    print("exception never occured, setting flag to 1")
finally:
    print("the code that always executes")
    
print("code continues")
