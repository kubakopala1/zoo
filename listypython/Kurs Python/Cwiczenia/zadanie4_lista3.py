import random

wylosowana_liczba = random.randint(0,100)
status = False
while status == False:
    liczba_uzytkownika = input("Podaj liczbe w przedziale od 0 do 100: ")
    roznica = abs(wylosowana_liczba-liczba_uzytkownika)
    if liczba_uzytkownika == wylosowana_liczba:
        print("Brawo udalo ci sie odganac liczbe {}".format(wylosowana_liczba))
        status = True
    if liczba_uzytkownika > wylosowana_liczba:
        if roznica >= 50:
            print("Liczba duzo mniejsza")
        elif roznica < 50 and roznica > 10:
            print("Liczba jest mniejsza")
        else:
            print("Liczba troche mniejsza")
    else:
        if roznica <= 50:
            print("Liczba jest duzo wieksza")
        elif roznica > 50 and roznica < 10:
            print("Liczba jest wieksza")
        else:
            print("Liczba jest troche wieksza")


