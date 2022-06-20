# all data & code is object
# classes & objects access data alike

class sample:
    """our fisrt class"""

    data_1 = 287
    data_2 = "monday"

    def funca():
        print("hello world")

obja = sample()
objb = sample()

print(obja.data_1)

# class name
sample.funca()

# error
obja.funca()
# sample.funca(obja)
