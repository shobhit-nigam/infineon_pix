# polymorphism

class time:
    def __init__(self, h=0, m=0):
        self.hours = h
        self.minutes = m

    def display(self):
        print(f"{self.hours} hours & {self.minutes} minutes")

    def __add__(self, other):
        total_min = self.hours*60 + self.minutes + other.hours*60 + other.minutes
        temp = time()
        temp.hours = total_min // 60
        temp.minutes = total_min % 60
        return temp

morn = time(1, 40)
noon = time(1, 50)
eve = time(0, 50)

total = morn + noon
            # total = time.__add__(morn, noon)

total.display()
