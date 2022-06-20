
class A:
    data1 = 100

    def method_a(self, val):
        print("updating value")
        self.data1 = val

    @classmethod
    def method_b(self, val):
        print("updating value")
        self.data1 = val

objx = A();
objy = A();
print(objx.data1)
print(objy.data1)
objx.method_b(200)
print(objx.data1)
print(objy.data1)
print(A.data1)
objz = A();
print(objz.data1)
