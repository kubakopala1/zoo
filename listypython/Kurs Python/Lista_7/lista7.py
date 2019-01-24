import konwerter_temperatur


def pobieranie_n():
    while True:
        n = raw_input("Podaj liczbe: ")
        if n.isdigit():
            break
    return n

def main():
    n = pobieranie_n()
    losowe_temperatury_celciusza = []
    for i in range(int(n)):
        temperatura_losowa = konwerter_temperatur.random_temp()
        losowe_temperatury_celciusza.append(temperatura_losowa)
    print losowe_temperatury_celciusza
    konwerter_temperatur.zapis_do_pliku("celsiusz.txt", losowe_temperatury_celciusza)
    print("Zadanie 3")
    wczytane_tenm_c = konwerter_temperatur.wczytaj_plik("celsiusz.txt")
    print("Wczytane temeratury celciusza: {}".format(wczytane_tenm_c))
    wczytane_temp_c = wczytane_tenm_c.split("\n")
    print wczytane_tenm_c
    for i in range(wczytane_temp_c.count("")):
        wczytane_temp_c.remove("")

    przekonwertowane_temp_f = []
    print(wczytane_temp_c)
    for temp_c in wczytane_temp_c:
        print(temp_c)
        temperatury_f = konwerter_temperatur.convert_celsius_to_fahrenheit(float(temp_c))
        przekonwertowane_temp_f.append(temperatury_f)
    konwerter_temperatur.zapis_do_pliku("farenheit.txt", przekonwertowane_temp_f)


main()
