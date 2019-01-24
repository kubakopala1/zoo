liczba1 = 3
liczba2 = 5
def funkcja(liczba1, liczba2):
    if liczba1 < liczba2:
        return liczba1
    else:
        return liczba2

funkcja(liczba1, liczba2)


def funkcja0(*pozycyjne):
    najmniejsza = pozycyjne[0]
    for element in pozycyjne:
        najmniejsza = funkcja(element, najmniejsza)

    return najmniejsza

print funkcja0(12,4,66,75,333)




