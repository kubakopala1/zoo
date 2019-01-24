import zadanie1_lista5

a1 = input("POdaj wspolczynnik a1: ")
r =  input("Podaj wspolczynnik r: ")
n = input("Podawj wspolczynnik n: ")

def nty_wyraz_ciagu(a1, r, n):
    wynik = zadanie1_lista5.ciag_artmetyczny(a1, r, n)
    return wynik

def oblicznie_sumy_pierwszych_n_wyrazow_ciagu(a1, r, n):
    wynik_sumy = zadanie1_lista5.suma_pierwszych_n_wyrazow_ciagu(a1, r, n)
    return wynik_sumy

def main():
    wynik = nty_wyraz_ciagu(a1, r, n)
    wynik_sumy = oblicznie_sumy_pierwszych_n_wyrazow_ciagu(a1, r, n)
    print("N-ty wyraz ciagu o wartosciach a1 = {}, r = {}, n = {}, jest rowny {}".format(a1, r, n, wynik))
    print("Suma pierwszych n wyrazow ciagu wynosi {}".format(wynik_sumy))

main()
