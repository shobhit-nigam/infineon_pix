# self
# self is not a keyword

class sample:
    """our fisrt class"""

    data_1 = 287
    data_2 = "monday"

    def funca(self):
        print("value of data_1 =", self.data_1)

obja = sample()
objb = sample()
obja.data_1 = 100
objb.data_1 = 88

obja.funca()
#sample.funca(obja)

objb.funca()
# sample.funca(objb)
