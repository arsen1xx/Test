class Eren:
    def __init__(self):
        self.nameeren = "Eren Yeager"
        self.ageeren = 19
        self.titaneren = "Attack titan, Founder titan, War hammer titan"
    def getinfo(self):
        a = input("Персонаж: ")
        if a.lower() == "eren":
            print(f"Name: {self.nameeren} \nAge: {self.ageeren} \nTitan: {self.titaneren} ")

class Armin:

    def __init__(self):
        self.namearmin = "Armin Arlert"
        self.agearmin = 19
        self.titanarmin = "Collosal titan"
    def info(self):
        b = input("Персонаж: ")
        if b.lower() == "armin":
            print(f"Name: {self.namearmin} \nAge: {self.agearmin} \nTitan: {self.titanarmin} ")
sigma = Eren()
sigma.getinfo()

sigma = Armin()
sigma.info()