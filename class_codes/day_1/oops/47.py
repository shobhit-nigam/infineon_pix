
class A:
    data1 = 100
    data2 = 300
#    def __str__(self):
#        return f"data1 and data2 values are = {self.data1}, {self.data2}"

    def __call__(self):
        print("data1 and data2 values are =", self.data1, self.data2)

    def __repr__(self):
        return f"class A(data1 = {self.data1}, data2 = {self.data2})"

objx = A();

print(objx)
