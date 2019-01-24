
def collatz(c0, n):
    ciagi_collatza = []
    ciagi_collatza.append(c0)
    cn = c0
    for i in range(1, n):
        if cn % 2 == 0:
            cn = cn*0.5
            ciagi_collatza.append(cn)
        else:
            cn = 3 * cn + 1
            ciagi_collatza.append(cn)
    return ciagi_collatza


def main():
    ciagi_collatza = collatz(11, 9)
    print ciagi_collatza
main()