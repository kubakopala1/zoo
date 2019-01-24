def podaj_dane():
    a1 = input("Podaj pierwsyz wyraz ciagu: ")
    q = input("Podaj iloraz: ")
    return a1, q


def wyliczanie_ciagu(a1, q):
    ciag = [a1]
    an = a1
    for i in range(9):
        an = an*q
        ciag.append(an)
    return ciag


def parzysta(lista):
    parzyste = []
    for liczba in lista:
        if liczba % 2 == 0:
            parzyste.append(liczba)
    return parzyste





def main():
    a1, q = podaj_dane()
    ciag= wyliczanie_ciagu(a1, q)
    print(ciag)
    print(len(ciag))
    parzyste = parzysta(ciag)
    print("Liczby parzyste w tym ciagu to: {}".format(parzyste))

main()



