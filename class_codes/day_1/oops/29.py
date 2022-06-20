# inheritance

class unix:
    def cmd(self):
        print("great command line")

    def security(self):
        print("rwx makes it more secure")

class linux(unix):
    def free(self):
        print("free & open source")

class android(linux):
    def ui(self):
        print("great ui")

obju = unix()
obju.cmd()
obju.security()
print("----")
objl = linux()
objl.cmd()
objl.security()
objl.free()
print("----")
obja = android()
obja.cmd()
obja.security()
obja.free()
obja.ui()
