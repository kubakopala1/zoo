
def ciag_geo(a1, q, n=100):
    lista_geo = []
    liczba = a1
    lista_geo.append(a1)
    for i in range(1, n):
        liczba = liczba * q
        lista_geo.append(liczba)
    return lista_geo

def liczby_pazyste(lista):
    lista_pazyste = []
    for i in lista:
        if i % 2 == 0:
            lista_pazyste.append(i)
    return lista_pazyste

def main():
    lista_geo = ciag_geo(1, 4, 100)
    lista_pazyste = liczby_pazyste(lista_geo)
    print lista_geo
    print lista_pazyste

main()