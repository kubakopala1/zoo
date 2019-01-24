def wczytywanie_pliku(file_name):
    with open(file_name, "r") as f:
        file_content = f.read()
    return file_content

def czesc_wspolna_list(lista1, lista2):
    wspolne_elementy = []
    for element in lista1:
        if element in lista2:
            if element not in wspolne_elementy:
                wspolne_elementy.append(element)

    return wspolne_elementy



def main():
    studenci_python_string = wczytywanie_pliku("studenci_python.txt")
    studenci_cpp_string = wczytywanie_pliku("studenci_cpp.txt")
    studenci_python = studenci_python_string.split("\n")
    studenci_cpp = studenci_cpp_string.split("\n")
    czesc_wspolna = czesc_wspolna_list(studenci_cpp, studenci_python)
    print czesc_wspolna
    print czesc_wspolna.count("Maria Dirac")
    print("lista studentow ktorzy uczeszczaja na oba wylady to: {}".format(czesc_wspolna))



main()


