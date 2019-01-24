import sys
import math

print sys.argv

def czy_prawidlowa():
    if len(p) != 4:
        print("Podales niewlasciwa ilosc argumentow")
        exit(1)


def obwod_trojkata(a, b, c):
    obwod = a + b + c
    return obwod

def pole_trojkata(a, b, c):
    obwod = obwod_trojkata(a, b, c)
    p = 0.5 * obwod
    pole = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return pole


def rodzaj(a, b, c):
    if a == b == c:
        print("Trojkat jest rownoboczny")
    if a == b or b == c or c == a:
        print("Trojkat jest rownoramienny")
    else:
        print("Trojkat jest roznoramienny")


def czy_trojkat(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        print("Z tego trojkata nie mozna zrobic trojkata")
        exit(1)



def dlugosci_bokow(a, b, c):
    lista = sorted([a, b, c])
    return lista

def rodzaj_kata(a, b, c):
    a, b, c = dlugosci_bokow(a, b, c)
    if (a**2 + b**2) == c**2:
        print("Trojkat jest prostokatny")
    elif (a**2 + b**2) < c**2:
        print("Trojkat jest rozwartokatny")
    elif (a**2 + b**2) > c**2:
        print("Trojkat jest ostrokatny")
    else:
        print("Nie mozna okreslic rodzaj trojkata")


def main():
    czy_prawidlowa()
    a, b, c = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]) # a,b,c = map(int, sys.argv[1:])
    czy_trojkat(a, b, c)
    obwod = obwod_trojkata(a, b, c)
    pole = pole_trojkata(a, b, c)
    rodzaj(a, b, c)
    rodzaj_kata(a, b, c)
    print(obwod)
    print(pole)


main()
