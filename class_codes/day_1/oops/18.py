
class A:
    def __init__(self, o, t):
        self.one = o
        self.two = t

    def add(self, t):
        self.three = t

objx = A(11, 22)
objy = A(100, "hello")

print("objx.one =", objx.one)
print("objy.one =", objy.one)
print("----")
print("objx.two =", objx.two)
print("objy.two =", objy.two)
print("----")
objx.add(77)
print("objx.three =", objx.three)
print("objy.three =", objy.three)
