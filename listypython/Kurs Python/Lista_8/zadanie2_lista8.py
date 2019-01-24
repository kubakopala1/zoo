import sys


def ciag_generator(n):
    ciag_gen = (float(i) / float(i + 1.0) for i in range(int(n)))
    return ciag_gen

def main():
    n = 1000
    ciag_gen = ciag_generator(n)
    print ciag_gen
    print next(ciag_gen)
    print next(ciag_gen)
    print next(ciag_gen)
    print next(ciag_gen)
    print next(ciag_gen)
    print next(ciag_gen)
    print sys.getsizeof(ciag_gen)
main()