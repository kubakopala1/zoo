
class Animal(object):
    def __init__(self):
        self.waga = 0
        self.wiek = 0
        self.gatunek = None
        self.imie = None

    def get_waga(self):
        return self.waga

    def get_wiek(self):
        return self.wiek

    def get_gatunek(self):
        return set.gatunek

    def get_imie(self):
        return self.imie

    def set_waga(self, value):
        self.waga = value

    def set_wiek(self, value):
        self.wiek = value

    def set_gatunek(self, value):
        self.gatunek = value

    def set_imie(self, value):
        self.imie = value


animal = Animal()

print animal.get_waga()
animal.set_waga(10)
print animal.get_waga()