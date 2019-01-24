warzywniak = {"cebula" : 1.50, "pomidor" : 2.40, "ziemniak" : 1.90, "burak" : 3.20, "por" : 2.10}

for key, value in warzywniak.items():
    print (key, value)

cena = (sum(warzywniak.values())/len(warzywniak.values()))
print("Srednia cena produktu wynosi: {}".format(cena))

warzywniak.update({"gorszek" : 1.14})
print warzywniak
cena = (sum(warzywniak.values())/len(warzywniak.values()))
print cena

del warzywniak["cebula"]
print warzywniak

cena = (sum(warzywniak.values())/len(warzywniak.values()))
print cena