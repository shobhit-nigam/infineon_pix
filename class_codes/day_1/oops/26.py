
class bank:
    acc_type = "savings"

    def __init__(self, n="john doe", o=0, a=None):
        self.name = n
        self.opn_bal = o
        self.acc_num = a
        self.cur_bal = o

    def display(self):
        print(f"welcome {self.name} your acc_num is {self.acc_num}")
        print(f"your {self.acc_type} account balance is {self.cur_bal}")

    def add_funds(self, amount):
        self.cur_bal = self.cur_bal + amount
        print(f"funds added, your update balance is {self.cur_bal}")

    def withdraw_funds(self, amount):
        if self.cur_bal >= amount:
            self.cur_bal = self.cur_bal - amount
            print(f"funds withdrawn your update balance is {self.cur_bal}")
        else:
            print("not enough balance")

    def __eligibility(self):
        if self.opn_bal > 1000:
            self.__grade = 'A'


obja = bank("bruce wayne", 1200, 345802)
objb = bank("tony stark", 1400)
objb.display()
print("-----")
obja.withdraw_funds(2000)
print("-----")
obja.add_funds(1000)
print("-----")
obja.withdraw_funds(2000)
