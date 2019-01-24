import random


def losuj_liczbe():
    losowa_liczba = random.randint(1000, 9999)
    return str(losowa_liczba)


def pobierz_liczbe():
    while True:
        podana_liczba = raw_input("Podaj liczbe cztercyfrowa ktore musza byc identyczne z podanym kluczem!: ")
        if len(podana_liczba) == 4 and podana_liczba.isdigit():
            break
        else:
            print("Podana liczba musi byc czterocyforwa!")
    return podana_liczba


def krowy(wylosowana_liczba, podana_liczba):
    licznik = 0
    for i in range(len(podana_liczba)):
        if wylosowana_liczba[i] == podana_liczba[i]:
            licznik += 1
    return licznik

def byki(wylosowana_liczba, podana_liczba):
    licznik = 0
    podana_liczba = [int(liczba) for liczba in podana_liczba]
    wylosowana_liczba = [int(liczba) for liczba in wylosowana_liczba]
    for i in range(len(podana_liczba)):
        if wylosowana_liczba[i] == podana_liczba[i]:
            podana_liczba[i] = None
            wylosowana_liczba[i] = None
    for i in range(len(podana_liczba)):
        if podana_liczba[i] == None:
            continue
        else:
            for j in range(len(wylosowana_liczba)):
                if podana_liczba[i] == wylosowana_liczba[j]:
                    licznik += 1
                    wylosowana_liczba[j] = None
                    break
    return licznik

# 5 9 9 9
# 1 1 5 5
# none 9 9 9

def main():
    wylosowana_liczba = losuj_liczbe()
    with open("wylosowanaliczba.txt", "w") as f:
        f.write(wylosowana_liczba)
    podana_liczba = pobierz_liczbe()
    while True:
        if podana_liczba == wylosowana_liczba:
            print("Brawo! udalo ci sie zgadnac liczbe")
            break
        else:
            liczba_krow = krowy(wylosowana_liczba, podana_liczba)
            print("Liczba Krow wynosi: {}".format(liczba_krow))
            liczba_bykow = byki(wylosowana_liczba, podana_liczba)
            print("Liczba Bykow wynosi: {}".format(liczba_bykow))
            podana_liczba = pobierz_liczbe()
main()

# funkcja krowy i byki oddzielnie i program na petli while
# uzytkownik ma podawac jedna liczbe 4cyfrowa

#def main():
#    liczba_wylosowana = losujj_liczbe_czterocyfrowa()
#    while
#    liczba_usera = pobierz_dane()
#    liczba_krow = licz_krowy(liczba_wylosowana, liczba_usera)
#    liczba_bykow = licz_byki(liczba_wylosowana, liczba_usera)
#    print "Liczba bykow: {}, Liczba krow: {}"