import random


def convert_celsius_to_fahrenheit(temp):
    t_fahrenheit = float(temp) * 1.8 + 32
    return round(t_fahrenheit, 2)


def convert_fahrenheit_to_celcius(temp):
    t_celsius = float(temp - 32) / 1.8
    return round(t_celsius, 2)


def convert_farenheit_to_kelwin(temp):
    f_to_kelwin = float(temp + 459.67) * 5/9
    return round(f_to_kelwin, 2)


def converter_celcius_to_kelwin(temp):
    c_to_kelwin = float(temp) + 273.15
    return round(c_to_kelwin, 2)


def random_temp():
    random_temp = random.uniform(-50.0, 50.0)
    return round(random_temp, 2)

def zapis_do_pliku(file_name, content):
    with open(file_name, "w") as f:
        if isinstance(content, list):
            for element in content:
                f.write("{}\n".format(element))
        else:
            f.write(str(content))

def wczytaj_plik(file_name):
    with open(file_name, "r") as f:
        content = f.read()
    return content





