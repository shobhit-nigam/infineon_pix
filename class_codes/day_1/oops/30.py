# inheritance
# overwrite

class unix:
    def cmd(self):
        print("great command line")

    def security(self):
        print("rwx makes it more secure")

class linux(unix):
    def free(self):
        print("free & open source")

    def new_cmd(self):
        self.cmd()
        print("pseudo terminals here")

obju = unix()
obju.cmd()
obju.security()
print("----")
objl = linux()
objl.new_cmd()
objl.security()
objl.free()
