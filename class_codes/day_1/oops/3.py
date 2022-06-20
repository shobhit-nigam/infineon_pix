# all data & code is object
# classes & objects access data alike

class sample:
    """our fisrt class"""

    data_1 = 287
    data_2 = "monday"

    def funca(self):
        print("hello world")

obja = sample()
objb = sample()

print(obja.data_1)
print(objb.data_1)
print(sample.data_2)

print(type(sample))
