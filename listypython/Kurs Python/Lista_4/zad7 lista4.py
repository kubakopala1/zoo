def funkcja(*pozycyjne, **kluczowe):
    for index, element in enumerate(pozycyjne):
        print "{} -> {}".format(index+1, element)
    for klucz, wartosc in kluczowe.iteritems():
        print "{} -> {}".format(klucz, wartosc)
funkcja(1, 2, 3, 4, argument1="aargument", argument2="aargument2", argument3="aargument3")
# *pozycyjne daje man możliwośc podawania nieskończonej liczby argumentów
# ""kluczowe daje nam możliwośc podawania dowolnej lości elementów klcuzowych
