from Animal import Animal

class Bird(Animal):
    def __init__(self):
        Animal.__init__(self)
        self.kolor = "Niebieski"

    def print_atrybuty(self):
        print self.kolor
        print self.gatunek
        print self.imie
        print self.waga
        print self.wiek

bird = Bird()

bird.print_atrybuty()


