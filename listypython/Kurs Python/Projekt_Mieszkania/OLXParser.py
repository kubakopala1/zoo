# coding: utf8
from bs4 import BeautifulSoup

class OLXParser(object):

    def __init__(self, html_text):
        self.html_text = html_text
        self.html_soup = BeautifulSoup(self.html_text, "html.parser")
        self.flats = self.find_flats()

    def find_flats(self):
        return self.html_soup.findAll("div", {"class": "offer-wrapper"})

    def collect_info_about_flats(self):
        for i, flat in enumerate(self.flats):
            title = self.find_title(flat)
            price = self.find_price(flat)
            flat_type = self.find_type(flat)
            district = self.find_ditrict(flat)
            print("{}. Tytul: {}, Cena: {}, Rodzaj: {}, Lokalizacja: {}".format(i+1, title, price, flat_type, district))


    def find_title(self, flat):
        title = flat.find("h3", {"class": "lheight22 margintop5"}).find("strong").getText().encode('utf-8')
        return title

    def find_price(self, flat):
        return flat.find("p", {"class": "price"}).find("strong").getText().encode('utf-8')

    def find_type(self, flat):
        return flat.find("small", {"class": "breadcrumb x-normal"}).getText().encode('utf-8').replace("Mieszkania » ", "").strip()

    def find_ditrict(self, flat):
        small_keys =  flat.findAll("small", {"class": "breadcrumb x-normal"})
        for small_key in small_keys:
            span_key = small_key.find("span")
            if span_key:
                if span_key.find("i", {"data-icon": "location-filled"}):
                    return span_key.getText().encode('utf-8').replace("\n", "")

