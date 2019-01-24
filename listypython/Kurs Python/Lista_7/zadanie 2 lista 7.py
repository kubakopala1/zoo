import konwerter_temperatur


def pobierz_dane():
    while True:
        podana_liczba = raw_input("Podaj dowolna liczbe: ")
        if podana_liczba.isdigit():
            break
        else:
            print("Przepraszam ale nie podales liczby calkowitej")
    return int(podana_liczba)


def main():
    n = pobierz_dane()
    temp_contener_celcius = []
    for i in range(n):
        temp_contener_celcius.append(konwerter_temperatur.random_temp())
    print("Wylosowane temperatury w celciuszach to: {}".format(temp_contener_celcius))

main() # with open na liscie 8 w teorii
