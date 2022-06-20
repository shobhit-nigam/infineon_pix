
class bank:

    def __init__(self, n, o, a):
        print("creating bank records")
        self.name = n
        self.opn_bal = o
        self.acc_num = a
        self.cur_bal = o

    def display(self):
        print(f"welcome {self.name}, your current balance is {self.cur_bal}")

obja = bank("bruce wayne", 1200, 345802)
objb = bank("tony stark", 1400, 346820)
print("-----")
obja.display()
objb.display()
