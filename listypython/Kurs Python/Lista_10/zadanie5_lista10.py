import argparse

def zapisywanie_do_pliku(nazwa_pliku, content):
    with open(nazwa_pliku, "a") as f:
        f.write("\n {}".format(content))

def arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', help="Sciezka do pliku", type=str,  required=True)
    parser.add_argument('--text', help="Tekst", type=str,  required=True)
    return parser.parse_args()

def main():
    arguments = arg_parse()
    zapisywanie_do_pliku(arguments.file, arguments.text)

main()

