import math


def dane_wejsciowe():
    a = input("Podaj wartosc a: ")
    b = input("Podaj wartosc b: ")
    c = input("Podaj wartosc c: ")
    return a, b, c

def wyliczanie_delty(a, b, c):
    delta = b**2 - 4*a*c
    return delta

def miejsca_zerowe(a, b, wynik_delty):
    if wynik_delty < 0:
        print "Funkcja nie ma miejsc zerowych"
    elif wynik_delty == 0:
        delta_zero = -b / 2*a
        print "Rownanie posiada jedno rozwiazanie {}".format(delta_zero)
    else:
        x1 = (-b - math.sqrt(wynik_delty) )/ 2*a
        x2 = (-b + math.sqrt(wynik_delty) )/ 2*a
        print "Rownanie posiada dwa rozwiazania {} i {}".format(x1, x2)


def main():
    a, b, c = dane_wejsciowe()
    print a, b, c
    wynik_delty = wyliczanie_delty(a, b, c)
    print wynik_delty
    miejsca_zerowe(a, b, wynik_delty)

if __name__ == '__main__':
    main()

