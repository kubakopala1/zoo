import matplotlib.pyplot as plt


class Samochod(object):

    def __init__(self, maksymalna_predkosc, spalanie):
        self.maksymalna_predkosc = maksymalna_predkosc
        self.spalanie = spalanie
        self.obecna_predkosc = 0
        self.pokonany_dystans = 0
        self.czas_podrozy = 0
        self.id_trasy = 1
        self.trasy = {}

#        {"1": "dystans":100, "czas":1, predkosc:100, "2": dystans:200, czas:2, predkosc 200}

#        { ID: dystans: X, PREDKOSC: Y, CZAS : Z, ID_2

#        ID DYSTANS CZAS PREDKOSC
#        1    100     1    100
#        2    200     2    200

    def przyspiesz(self, przyspiesz_auto):
        przyspiesz_auto = self.obecna_predkosc + przyspiesz_auto
        if przyspiesz_auto > self.maksymalna_predkosc:
            print("Predkosc auta jest zbyt duza!")
            przyspiesz_auto = self.maksymalna_predkosc
        self.obecna_predkosc = przyspiesz_auto



    def zwolnij(self, zwolnij_auto):
        zwolnij_auto = self.obecna_predkosc - zwolnij_auto
        if zwolnij_auto < 0:
            print("Auto zwolinlo do zera!")
            zwolnij_auto = 0
        self.obecna_predkosc = zwolnij_auto

    def hamuj(self):
        self.obecna_predkosc = 0

    def turbo(self):
        self.obecna_predkosc = self.maksymalna_predkosc

    def jedz(self, dystans_do_przebycia):
        if self.obecna_predkosc == 0:
            print("Obecna predkosc jest rowna 0!")
        else:
            czas_podrozy = float(dystans_do_przebycia) / float(self.obecna_predkosc)
            self.pokonany_dystans += dystans_do_przebycia
            self.czas_podrozy += czas_podrozy
            self.dodaj_trase()


    def podroz(self):
        srednia_predkosc = self.pokonany_dystans / self.czas_podrozy
        spalanie =self.pokonany_dystans / self.spalanie
        print("Calkowity pokonany dystans: {}\n Czas podrozy: {}\n Srednia predkosc: {}\n Ilosc spalonej benzyny: {} litrow".format(self.get_pokonany_dystans(), self.get_czas_podrozy(), srednia_predkosc, spalanie))


    def dodaj_trase(self):
        self.trasy[self.id_trasy] = {"dystans": self.pokonany_dystans, "czas": self.czas_podrozy, "predkosc": self.obecna_predkosc}
        self.id_trasy += 1
        print self.trasy

    def rysuj_wykres_drogi_od_czasu(self):
        lista_dystanse_tras = []
        lista_czas_tras = []
        for i in range(1, self.id_trasy):
            print(i)
            dystans_trasy = self.trasy.get(i).get("dystans")
            lista_dystanse_tras.append(dystans_trasy)
        for i in range(1, self.id_trasy):
            czasy_trasy = self.trasy.get(i).get("czas")
            lista_czas_tras.append(czasy_trasy)

        plt.plot(lista_czas_tras, lista_dystanse_tras)
        plt.grid()
        plt.xlabel("Czas podrozy[h]")
        plt.ylabel("Pokonany dystans[km]")
        plt.title("Wykres drogi od czasu")
        plt.show()

    def rysuj_wykres_predkosci_od_czau(self):
        lista_predkosci_tras = []
        lista_czas_tras = []
        for i in range(1, self.id_trasy):
            predkosci = self.trasy.get(i).get("predkosc")
            lista_predkosci_tras.append(predkosci)
        for i in range(1, self.id_trasy):
            czasy_trasy = self.trasy.get(i).get("czas")
            lista_czas_tras.append(czasy_trasy)
            # x = [wartosc['czas'] for wartosci in self.wszystkie_trasy.values()]

        plt.plot(lista_czas_tras, lista_predkosci_tras)
        plt.grid()
        plt.ylabel("Predkosci[km/h]")
        plt.xlabel("Czas podrozy[h]")
        plt.title("Stosunek predkosci od czasu")
        plt.show()



    def get_obecna_predkosc(self):
        return self.obecna_predkosc

    def get_maksymalna_predkosc(self):
        return self.maksymalna_predkosc

    def get_spalanie(self):
        return self.spalanie

    def get_pokonany_dystans(self):
        return self.pokonany_dystans

    def get_czas_podrozy(self):
        return self.czas_podrozy




samochod = Samochod(220, 10)
print("Samochod aktualnie jedzie {} km/h, jego maksymalna predkocs to: {}, jego spalanie jest rowne: {}".format(samochod.get_obecna_predkosc(), samochod.get_maksymalna_predkosc(), samochod.get_spalanie()))
samochod.przyspiesz(120)
print("Samochod aktualnie jedzie {} km/h, jego maksymalna predkocs to: {}, jego spalanie jest rowne: {}".format(samochod.get_obecna_predkosc(), samochod.get_maksymalna_predkosc(), samochod.get_spalanie()))
samochod.zwolnij(80)
print("Samochod aktualnie jedzie {} km/h, jego maksymalna predkocs to: {}, jego spalanie jest rowne: {}".format(samochod.get_obecna_predkosc(), samochod.get_maksymalna_predkosc(), samochod.get_spalanie()))
samochod.jedz(200)
print("Samochod aktualnie jedzie {} km/h, jego maksymalna predkocs to: {}, jego spalanie jest rowne: {}.Pokonany dystans to: {} w czasie {}".format(samochod.get_obecna_predkosc(), samochod.get_maksymalna_predkosc(), samochod.get_spalanie(), samochod.get_pokonany_dystans(), samochod.get_czas_podrozy()))
samochod.podroz()
samochod.jedz(40)
samochod.przyspiesz(300)
samochod.jedz(50)
samochod.hamuj()
samochod.jedz(30)
samochod.podroz()
samochod.rysuj_wykres_drogi_od_czasu()
samochod.rysuj_wykres_predkosci_od_czau()


