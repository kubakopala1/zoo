
def ciag_artmetyczny(a1,r,n):
    wynik = a1 + (n-1)*r
    return wynik

def suma_pierwszych_n_wyrazow_ciagu(a1, r, n):
    wyniki = [a1]
    for i in range(2, n+1):
        wynik = ciag_artmetyczny(a1, r, i)
        wyniki.append(wynik)
    return sum(wyniki)



print("Suma pierwszych wyrazow ciagu jest rowna: {}".format(suma_pierwszych_n_wyrazow_ciagu(1,2,5)))