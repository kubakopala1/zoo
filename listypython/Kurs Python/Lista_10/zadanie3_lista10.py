def liczenie_objetosci(a, b=None, c=None):
    if b==None and c == None:
        wynik = pow(a,3)
        print("objetosc szcianu wynosi: {}".format(wynik))
    else:
        wynik = int(a)*int(b)*int(c)
        print("Objetosc prostopdaloscianu wynoski: {}".format(wynik))

liczenie_objetosci(3,2,3)