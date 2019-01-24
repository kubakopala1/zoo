# zadanie 2, 3, 4
# zadanie 2
print("zadanie 2")
kwadraty = [x**2 for x in range(10)]
print(kwadraty)
for i, item in enumerate(kwadraty):
    print("{} -> {}".format(i,item))
 # zadanie 3

print("Zadanie 3")

i = 0
while i < 10:
    if i % 2 ==0:
        print(i)
    i += 1



# zadanie 4
print("Zadanie 4")

grocery = ['jajka', 'mleko', 'chleb', 'maslo', 'piwo']

n_items = {}

prohibited = ['wodka', 'piwo', 'wino']

for product in grocery:

    if product in prohibited:
        ilosc = 0
    else:
        ilosc = input("Produkt {}: sztuk = ".format(product))
    n_items.update({product : ilosc})
print n_items

for i, (key, value) in enumerate(n_items.items()):

    print("{}. {} : {}".format(i+1, key, value))

