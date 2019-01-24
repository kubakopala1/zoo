def nty_wyraz_ciagu(a1, r, n):
    wynik = a1 + (n -1)*r
    return wynik


def suma_pierwszych_n_wyrazow_ciagow(a1, r, n):
    wyniki = [a1]
    for i in range(2, n+1):
        wynik = nty_wyraz_ciagu(a1, r, i)
        wyniki.append(wynik)
    return sum(wyniki)

print suma_pierwszych_n_wyrazow_ciagow(1, 2, 5)
