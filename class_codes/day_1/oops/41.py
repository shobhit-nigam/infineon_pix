# polymorphism

class time:
    def __init__(self, h, m):
        self.hours = h
        self.minutes = m

    def display(self):
        print(f"{self.hours} hours & {self.minutes} minutes")

morn = time(1, 40)
noon = time(1, 50)
eve = time(0, 50)

morn.display()

#error
total = morn + noon
