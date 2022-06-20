
class A:
    data1 = 100
    data2 = 300

    def __init__(self):
        print("called during creation")

    def __del__(self):
        print("called during deletion")

objx = A();

print(objx.data1)
