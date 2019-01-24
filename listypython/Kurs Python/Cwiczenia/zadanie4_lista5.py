
def pierwsze_wystapienie_liczby_jeden(c0, n):
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
        if cn == 1:
            break
    return ciagi_collatza

def main():
    ciagi_collatza = pierwsze_wystapienie_liczby_jeden(10, 8)
    print ciagi_collatza

main()