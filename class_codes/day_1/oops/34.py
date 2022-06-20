# inheritance

class unix:
    def cmd(self):
        print("great command line")

    def security(self):
        print("rwx makes it more secure")

class linux(unix):
    def free(self):
        print("free & open source")

    def stable(self):
        print("pretty stable")

class mobile_os:
    def portability(self):
        print("highly portable & scalable")

    def stable(self):
        print("sometimes unstable")

class android(mobile_os, linux):
    def ui(self):
        print("great ui")

obja = android()

print(issubclass(android, linux))
print(issubclass(android, unix))
print(issubclass(bool, int))
print(issubclass(int, float))
