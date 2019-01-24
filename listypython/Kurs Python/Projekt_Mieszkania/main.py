import requests
from OLXParser import OLXParser
from OTODOMParser import OTODOMParser

def main():
    print("Mieszkania OLX")
    olx = requests.get("https://www.olx.pl/nieruchomosci/mieszkania/wroclaw/")
    olx_parser = OLXParser(olx.text)
    olx_parser.collect_info_about_flats()
    print("Mieszkania OtoDom")
    otodom = requests.get("https://www.otodom.pl/sprzedaz/mieszkanie/wroclaw/")
    otodom_parser = OTODOMParser(otodom.text)
    otodom_parser.collect_info_about_flats1()
main()