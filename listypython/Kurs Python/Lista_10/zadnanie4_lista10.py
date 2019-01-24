pobrany_tekst = raw_input("Wpisz dowolny teskt: ")
samogloski = ["a","i","e","y","u","s","o",]
for samogloska in samogloski:
    print("Liczba samoglosek {} w podanym tekscie wynosi {}".format(samogloska, pobrany_tekst.count(samogloska)))
