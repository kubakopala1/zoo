def fibonaci(n):
    a = 0
    b = 1
    print("Wyraz numer:", 0, "Wartosc:", a)
    print("wyraz numer:", 1, "Wartosc:", b)
    for i in range(0, n - 1):
        a, b = b, a + b
        print("Wyraz numer:", i + 2, "Wartosc:", b)

fibonaci(10)
