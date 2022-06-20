
class A:
    data1 = 100

    def method_a(self, val):
        print("updating value")
        self.data1 = val

    @classmethod
    def method_b(cls, val):
        print("updating value")
        cls.data1 = val

    @staticmethod
    def method_c(val):
        print("static method, val =", val)

objx = A();
objx.method_c(500)
print(A.data1)
