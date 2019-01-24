import random

def losowa():
    losowa = random.randint(0,100)
    return losowa
wynik = losowa()
print wynik
status = False
while status == False:
    liczba = input("Zgadnij liczbe: ")
    roznica = abs(liczba - wynik)   #liczba 30 wynik 50    20
    if liczba == wynik:
        print("Zgadles i nic nie wygrasz i tak")
        status = True
        break
    if liczba > wynik:
        if roznica > 50:
            print("Liczba jest duzo mniejsza")
        if roznica > 10 and roznica < 50:
            print("Liczba jest mniejsza")
        if roznica < 10:
            print("Liczba jest troszke mniejsza")
    else:
        if roznica < 10:
            print("Liczba jest torche wyzsza")
        if roznica > 10 and roznica < 50:
            print("Liczba jest wyzsza")
        if roznica > 50:
            print("Liczba jest dużo wyzsza")

