
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

obja = bank()
print(obja.name)
obja.open("bruce wayne", 1200, 345802)
print(obja.name)
