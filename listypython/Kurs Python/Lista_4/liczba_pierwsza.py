def pobierz_dane():
    while True:
        podana_liczba = raw_input("Podaj dowolna liczbe: ")
        if podana_liczba.isdigit():
            break
        else:
            print("Przepraszam ale nie podales liczby calkowitej")
    return podana_liczba

def czy_pierwsza(podana_liczba):
    status = True
    for i in range(2, podana_liczba):
        if podana_liczba % i == 0:
            status = False
    return status


def main():
    podana_liczba = pobierz_dane()
    status = czy_pierwsza(int(podana_liczba))
    print status

main()
