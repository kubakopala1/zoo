def ciag_look_and_say(ciag):
    ciag = "1211"
    cyfra = ciag[0]
    licznik = 0
    nowy_ciag = ""
    for liczba in ciag:
        if liczba == cyfra:
            licznik +=1
        else:
            nowy_ciag ="{}{}{}".format(nowy_ciag, licznik, cyfra)
            cyfra = liczba
            licznik = 1
    nowy_ciag = "{}{}{}".format(nowy_ciag, licznik, cyfra)
    return nowy_ciag

def ciag_look_and_say_2(ciag):
    ciag = "1211"
    # nowy_ciag = ["1", "2", "11"]
    nowy_ciag = []
    cyfra = ciag[0]
    nowy_ciag_2 = []
    nowa_cyfra = "{}".format(cyfra) # ciag[0]
    for i in range(1,len(ciag)):
        if ciag[i] == cyfra:
            nowa_cyfra = nowa_cyfra + ciag[i]
        else:
            nowy_ciag.append(nowa_cyfra)
            cyfra = ciag[i]
            nowa_cyfra = ciag[i]
    nowy_ciag.append(nowa_cyfra)
    for pozycja in nowy_ciag:
        nowy_ciag_2.append(str(len(pozycja)) + pozycja[0])
    return ''.join(nowy_ciag_2)




print ciag_look_and_say_2(1211)