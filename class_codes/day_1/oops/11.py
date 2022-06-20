
class bank:
    name = "john doe"
    opn_bal = 0
    cur_bal = opn_bal
    acc_num = 0

    def open(self, n, o, a):
        print("creating bank records")
        self.name = n
        self.opn_bal = o
        self.acc_num = a
        self.cur_bal = o

    def display(self):
        print(f"welcome {self.name}, your current balance is {self.cur_bal}")

obja = bank()
objb = bank()
obja.display()
objb.display()
print("-----")
obja.open("bruce wayne", 1200, 345802)
obja.display()
objb.display()
