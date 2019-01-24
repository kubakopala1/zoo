def pobierz_dane():
    c0 = input("Podaj c0: ")
    n = input("Podaj n: ")
    return c0, n


def czy_pazysta(liczba):
    if liczba % 2 == 0:
        return True
    return False

def collatz(c0, n):
    cn = c0
    for i in range(n):
        if czy_pazysta(cn):
            cn = 0.5*cn
        else:
            cn = 3*cn+1
    return cn


def jeden_collatza(c0, n):
    cn = c0
    n = 0
    while cn != 1:
        if czy_pazysta(cn):
            cn = 0.5 * cn
        else:
            cn = 3 * cn + 1
        n += 1
    return cn, n


def main():
    c0, n = pobierz_dane()
    cn = collatz(c0, n)
    print(cn)
    #zadanie 4
    cn, n = jeden_collatza(c0, n)
    print cn, n



main()
# w zanukruj w  pythonie doczytac argymenty funckji
# zadanie5 i funkcja map
# wyliczanie liczby pierwszej : czy 6 jest liczba pierwsza ?  dzielimy 6 przez 6, 1