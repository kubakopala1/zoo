
class Calculator():

        def dodaj(self, a, b):
            wynik = a + b
            print(wynik)
        def odejmij(self, a, b):
            wynik = a - b
            print(wynik)
        def iloczyn(self, a, b):
            wynik = a * b
            print(wynik)
        def iloraz(self, a, b):
            wynik = a / b
            print(wynik)
        def podnies_do_potegi(self, a, b):
            wynik = pow(a,b)
            print(wynik)

calc = Calculator()
calc2 = Calculator()

calc.dodaj(2,2)
calc2.podnies_do_potegi(2,8)