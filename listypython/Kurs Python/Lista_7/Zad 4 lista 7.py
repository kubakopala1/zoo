import konwerter_temperatur


def czy_identyczne():
    status = False
    if c_to_kelwin[0] != f_to_kelwin[0]:
        status = True
    return status

def clean_list(data_list):
    for i in range(data_list.count("")):
        data_list.remove("")
    return data_list

def compare_two_list(list1, list2):
    len_list1 = len(list1)
    len_list2 = len(list2)
    if len_list1 != len_list2:
        print("Nie mozna porownac list, ich wymiary sa rozne")
        exit(1)

    for i in range(len_list1):
        if list1[i] != list2[i]:
            print("Wartosci {} oraz {} sa rozne".format(list1[i], list2[i]))
            exit(1)
    print("Wszystkie elementy dwoch list sie zgadzaja!")

def main():
    print("Wczytane pliki: ")
    f_wczytywanie_z_pliku = clean_list(konwerter_temperatur.wczytaj_plik("farenheit.txt").split("\n"))
    c_wczytywanie_z_pliku = clean_list(konwerter_temperatur.wczytaj_plik("celsiusz.txt").split("\n"))
    print f_wczytywanie_z_pliku
    c_to_kelwin = []
    f_to_kelwin = []
    for temp_c in c_wczytywanie_z_pliku:
        c_to_kelwin.append(konwerter_temperatur.converter_celcius_to_kelwin(float(temp_c)))

    for temp_f in f_wczytywanie_z_pliku:
        f_to_kelwin.append(konwerter_temperatur.convert_farenheit_to_kelwin(float(temp_f)))
    compare_two_list(c_to_kelwin, f_to_kelwin)
    print c_to_kelwin
    print f_to_kelwin

main()