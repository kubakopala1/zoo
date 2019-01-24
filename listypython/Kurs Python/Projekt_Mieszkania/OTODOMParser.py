# coding: utf8
from bs4 import BeautifulSoup

class OTODOMParser(object):
    def __init__(self, html_text):
        self.html_text = html_text
        self.html_soup = BeautifulSoup(self.html_text, "html.parser")
        self.flats = self.find_flats()

    def find_flats(self):
        return self.html_soup.findAll("div", {"class": "offer-item-details"})

    def collect_info_about_flats1(self):
        for i, flat in enumerate(self.flats):
            title = self.find_title(flat)
            price = self.find_price(flat)
            flat_type = self.find_type(flat)
            district = self.find_district(flat)
            print("{}. Tytuł: {}, Cena: {}, Rodzaj: {}, Lokalizacja: {}".format(i+1, title, price, flat_type, district))


    def find_title(self, flat):
        title = flat.find("span", {"class": "offer-item-title"}).getText().encode('utf-8')
        return title

    def find_price(self, flat):
        price = flat.find("li", {"class": "offer-item-price"}).getText().encode('utf-8').strip()
        return price

    def find_district(self, flat):
        district = flat.find("p", {"class": "text-nowrap hidden-xs"}).getText().encode('utf-8').replace("Mieszkanie na sprzedaż: ", "")
        return district

    def find_type(self, flat):
        flat_type = flat.find("li", {"class": "offer-item-price"}).getText().encode('utf-8').strip()
        if flat_type > 50000:
            flat_type = "Sprzedaż"
        else:
            flat_type = "Wynajem"
        return flat_type
