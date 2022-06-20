lista = [33, 76, 90, 12, 54, 67]
index = 0

try:
    age = int(input("enter the index here: \n"))
    if age < 18:
        raise ValueError
    print("all good")
except ValueError:
    print("age should be greater than 18")


print("code continues")
