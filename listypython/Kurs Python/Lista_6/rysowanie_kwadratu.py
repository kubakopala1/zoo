#!/usr/bin/env python

import turtle

length = eval(input("Podaj dł\lugosc boku: "))
n_sides = 4 # ilosc boków

turtle.speed(20) # ustal predkosc zolwia

# powtorz n_sides razy
for i in range(n_sides):
    turtle.forward(length) # narysuj linie o danej dlugosci
    turtle.right(90)       # obroc sie w prawo o dany kat

turtle.mainloop() # nie zamykaj okna po narysowaniu