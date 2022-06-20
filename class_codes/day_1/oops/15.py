
class bank:
    acc_type = "savings"

    def __init__(self, n="john doe", o=0, a=None):
        print("creating bank records")
        self.name = n
        self.opn_bal = o
        self.acc_num = a
        self.cur_bal = o

    def display(self):
        print(f"welcome {self.name} your acc_num is {self.acc_num}")
        print(f"your {self.acc_type} account balance is {self.cur_bal}")

obja = bank("bruce wayne", 1200, 345802)
objb = bank("tony stark", 1400)
print("-----")
obja.display()
objb.display()
print("-----")
print(type(obja))
