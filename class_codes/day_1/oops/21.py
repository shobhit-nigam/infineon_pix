
class A:
    def __init__(self, o, t):
        self.one = o
        self.two = t

    def add(self, t):
        self.three = t

objx = A(100, 200)


########## not part of class
def gen(self):
    print("defined outside")

objx.sub = gen

objx.sub("hi")
