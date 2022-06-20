# inheritance

class unix:
    def cmd(self):
        print("great command line")

    def security(self):
        print("rwx makes it more secure")

class linux(unix):
    def free(self):
        print("free & open source")

class mobile_os:
    def portability(self):
        print("highly portable & scalable")

class android(linux, mobile_os):
    def ui(self):
        print("great ui")

obja = android()
obja.cmd()
obja.security()
obja.free()
obja.ui()
obja.portability()
