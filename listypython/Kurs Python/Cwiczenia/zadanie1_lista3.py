
lista_skladana = range(1,100)
print lista_skladana
print [pow(liczba,2) for liczba in lista_skladana]

for i, item in enumerate(lista_skladana):
    print("{} -> {}".format(i, item))