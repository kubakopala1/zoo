import ciag_artmetyczny

def pobierz_dane():
    a1 = input("Podaj pierwszy wyraz ciagu: ")
    r = input("Podaj roznice: ")
    n = input("Podaj n-ty wyraz ciagu:")
    return a1, r, n

def main():
    a1, r, n = pobierz_dane()
    nty_wyraz_ciagu = ciag_artmetyczny.nty_wyraz_ciagu(a1, r, n)
    suma = ciag_artmetyczny.suma_pierwszych_n_wyrazow_ciagow(a1, r, n)
    print("Suma pierwszych n wyrazow ciagow to: {}".format(suma))
    print("N-ty wyrazow ciagow to: {}".format(nty_wyraz_ciagu))

main()

