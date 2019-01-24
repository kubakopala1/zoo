def funkcja(liczba1, liczba2):
    if liczba1 < liczba2:
        return liczba1
    else:
        return liczba2

def mniejsza_args(*liczby):
    najmniejsza = liczby[0]
    for liczba in liczby:
        najmniejsza = funkcja(najmniejsza,liczba)
    print(najmniejsza)

mniejsza_args(122,5,677,8,52,111,1.1)
