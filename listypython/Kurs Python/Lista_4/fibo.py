def fibonacci(n):
    a, b = 0, 1
    print "{} -> {}".format(0, a)
    print "{} -> {}".format(1, b)
    for i in range(2,n+1):
        a, b = b, a+b
        print "{} -> {}".format(i, b)

fibonacci(4)
