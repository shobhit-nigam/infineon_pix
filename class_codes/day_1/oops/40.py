# polymorphism

class cricket:
    def __init__(self, overs, bowls):
        self.overs = overs
        self.bowls = bowls

    def display(self):
        print(f"{self.overs} overs and {self.bowls} bowls bowled")

player1 = cricket(3, 4)
player2 = cricket(2, 5)
# error
player3 = player1 + player2
player3.display()
