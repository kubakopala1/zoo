import sys

print ("ZADANIE 1 IISTA 2---------------------------------------------")
tuple = ("jeden", "dwa", "trzy", "cztery", 5, 6, 7, 8, 9)
print tuple[:3]
print tuple[-2:]
print tuple[1::2]
print len(tuple)
print tuple[:4] + (1000, 1001) + tuple[-5:]

print ("ZADANIE 2 IISTA 2---------------------------------------------")
studenci = ['Kasia', 'Basia', 'Marek', 'Darek']
print studenci
studenci.append('Jozek')
print studenci
studenci.extend(["Basia","Ania"])
print studenci
print sorted(studenci)
studenci.remove("Basia")
studenci.remove("Basia")
print studenci
print len(studenci)

print("ZADANIE3 LISTA2---------------------------------------------")
lista = range(3,100,3)
print lista
del lista[5::3]
print lista
print sum(lista)/ len(lista)

print("ZADANIE4 LISTA2---------------------------------------------")
krotka = ('a', 'b', 'c', 'd')
print krotka
print("\t".join(str(0) for i in range(100)))

print("ZADANIE5 LISTA2---------------------------------------------")
slubowanie = """
wstepujac do wspolnoty akademickiej Uniwersytetu Wroclawskiego, slubuje uroczyscie:
- zdobywac wiedze i umiejetnosci,
- postepowac zgodnie z prawem, tradycja i dobrymi obyczajami akademickimi,
- dbac o dobre imie Uniwersytetu Wroclawskiego i godnosc studenta.
"""
print slubowanie.upper()
spojnik_i = (slubowanie.count(" i "))
print("Liczba i w teskcie to: ")
print(spojnik_i)
liczba_i = (slubowanie.count("i"))
print("Liczba liter i w tekscie to: ")
print(liczba_i)
print("Czy w tekscie znajduje sie wyraz Uniwersytet: ")
print("Uniwersytet" in slubowanie)

print("ZADANIE6 LISTA2---------------------------------------------")
print("Ile pamieci zajmuje liczba 0: ")
print(sys.getsizeof(0))
print("Ile pamieci zajmuje liczba 2**100: ")
print(sys.getsizeof(2**100))
print("Ile pamieci zajmuje liczba 2*1000: ")
print(sys.getsizeof(2*1000))
print("Ile pamieci zajmuje True i False: ")
print(sys.getsizeof(True))
print(sys.getsizeof(False))

print(isinstance(0, int))
print(isinstance(0, float))
print(isinstance(0.0, float))
print(isinstance(True, bool))
print(isinstance(True, int)) #true dziala dokladnie jak 1(czyli int)

print("ZADANIE8 LISTA2---------------------------------------------")
print("Wersja pierwsza: ")
x = (a, b, c) = (1, 2, 3)
print(a)
print(b)
print(c)
print("Wersja druga: ")
y = a, b, c = 1, 2, 3
print(a)
print(b)
print(c)
print("Zamiana wartosci: ")
c = 1
v = "Jeden"
print(c)
print(v)
c = v
print(c)
print(v)

print("ZADANIE1 LISTA4---------------------------------------------")
produkty = {'jablko': 4.25, "gruszka": 2.7, "pamarancz":1.25, "arbuz":7.2}
for key, values in produkty.items():
    print(key, values)

srednia_cena_produktu = float(sum(produkty.values())) / float(len(produkty.values()))
print("Srednia cena produktu wynosi: ")
print(srednia_cena_produktu)

produkty.update({'cytryna': 5.60})
print(produkty)
print("Srednia cena produktu wynosi: ")
print(float(sum(produkty.values())) / float(len(produkty.values())))
del produkty["arbuz"]
print(produkty)
print("Srednia cena produktu wynosi: ")
print(float(sum(produkty.values())) / float(len(produkty.values())))

print("ZADANIE2 LISTA4---------------------------------------------")

def mniejsza(a, b):
    if (a > b):
        print(a)
    else:
        print(b)

mniejsza(14,15)

print("ZADANIE3 LISTA4---------------------------------------------") # do ogarniecia!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def mniejsza_liczba(*liczby):
    najmniejsza = liczby[0]
    liczba = (*liczby)
    for liczba in liczby:
        if i < najmniejsza:
            print i

mniejsza_liczba(4,6,33,89,0)

print("ZADANIE4 LISTA4---------------------------------------------")

def fibonacci():

