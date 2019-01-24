import argparse


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', help='Path to file', type=str, required=True)
    parser.add_argument('--mode', help = 'Mode how to read file, 0 - (default choise), read whole file - 1, omit lines with # at the beginning, 2 line numbering ', choices=[0, 1, 2], default=0, type=int)
    return parser.parse_args()

def wczytaj_plik(file_name):
    with open(file_name, "r") as f:
        file_content = f.read()
    return file_content

def drukuj_tekst(text, mode):
    if mode == 0:
        print text
    elif mode == 1:
        splitted_text = text.split("\n")
        for row in splitted_text:
            if not row.startswith("#"):
                print row
    elif mode ==2:
        splitted_text = text.split("\n")
        for i, value in enumerate(splitted_text):
            print("{}. {}".format(i+1, value))


def main():
    arguments = arg_parser()
    print(arguments.file)
    print(arguments.mode)
    file_content = wczytaj_plik(arguments.file)
    drukuj_tekst(file_content, arguments.mode)

main()