# inheritance

class unix:
    def __init__(self):
        print("init of unix")

    def cmd(self):
        print("great command line")

    def security(self):
        print("rwx makes it more secure")

class linux(unix):
    def free(self):
        print("free & open source")

obju = unix()
print("----")
objl = linux()
