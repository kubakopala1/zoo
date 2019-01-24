import math


def dane_wejsciowe():
    a = input("Podaj wspolczynnik a: ")
    b = input("Podaj wspolczynnik b: ")
    c = input("Podaj wspolczynnik c: ")
    return a,b,c

def wyliczanie_delty(a,b,c):
    delta = ((b**2) - 4*a*c)
    return delta

def miejsca_zerowe(delta, a, b):
    if delta > 0:
        x1 = float(-b - math.sqrt(delta)) / float(2 * a)
        x2 = float(-b + math.sqrt(delta)) / float(2 * a)
        print("Rownanie kwadratowe posiada dwa miejsca zerowe {} oraz {}".format(x1,x2))
    elif delta == 0:
        x0 = float(-b) / float(2 * a)
        print "Rownanie kwadratowe posiada jedno rozwiazanie: x0 {}".format(x0)
    else:
        print "Rownanie kwadratowe nie posiada rozwiazan w zbiorze liczb rzeczywistych dla delta < 0."

def main():
    a,b,c = dane_wejsciowe()
    delta = wyliczanie_delty(a,b,c)
    print("Wspolczynniki a, b, c kolejno to: {}, {}, {}".format(a, b, c))
    print("Delta jest rowna: {}".format(delta))
    miejsca_zerowe(delta, a, b)

main()