# encapsulation

class A:
    data1 = 100
    _data2 = 200
    # hidden
    # similar to private
    __data3 = 300
    __data4__ = 400

    def display(self):
        print("data1 =", self.data1)
        print("data2 =", self._data2)
        print("data3 =", self.__data3)
        print("data4 =", self.__data4__)

obja = A()

print("data1 =", obja.data1)
print("data2 =", obja._data2)
#print("data3 =", obja.__data3)
print("data4 =", obja.__data4__)
