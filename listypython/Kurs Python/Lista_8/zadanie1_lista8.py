import sys


def pobierz_dane():
    while True:
        liczby = raw_input("Podaj n: ")
        if liczby.isdigit():
            return liczby
        else:
            print("Nie podales liczby!")

def ciag(n):
    ciag_lista = [float(i)/float(i+1.0) for i in range(int(n))]
    return ciag_lista

def zapis_do_pliku(nazwa_pliku, zawartosc):
    with open(nazwa_pliku, "w") as f:
        if isinstance(zawartosc, list):
            for element in zawartosc:
                f.write("{}\n".format(element))
        else:
            f.write(zawartosc)

def main():
    liczby = pobierz_dane()
    ciag_lista = ciag(liczby)
    zapis_do_pliku("Lista.txt", ciag_lista)
    print sys.getsizeof(ciag_lista)

main()