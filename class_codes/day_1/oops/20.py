
class A:
    def __init__(self, o, t):
        self.one = o
        self.two = t

    def add(self, t):
        self.three = t

objx = A(100, 200)

######## adding (defining) functions outside the class

def gen(self):
    print("defined outside")

A.sub = gen

A.sub("")
objx.sub()
