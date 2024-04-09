#szit.hu/int helye
print("Dobány Norbert, 2023-12-06")
print("Ágazati 001 mintafeladat megoldása")
print("Csapadék mennyiség milliméterben: ")
heti = int(input("Aktuális heti csapadék: "))
mult = int(input("Előző heti csapadék: "))
if heti<mult:
    print("Kevesebb csapadék")
elif heti==mult:
    print("Nem változott")
else:
    print("Több csapadék")