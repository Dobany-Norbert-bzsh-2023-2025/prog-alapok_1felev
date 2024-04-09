#IDE KELL A szit.hu/int SZÖVEG!!!

print("Ut hosszanak vizsgalata")

while input("akarsz még?")!="n":
    hossz = float(input("Milyen hosszu az ut?"))
    with open('1/output.txt', 'a', encoding='utf-8') as f:
        if hossz>1:
            f.write("Tul hosszu:")
        else:
            f.write("Megfelelo:")
        f.write(f"{str(hossz)}")
        f.write("\n")


with open('1/output.txt','r',encoding='utf-8') as f:
    lines = f.readlines()

#ÖSSZEGZÉS
sum=0
for line in lines:
    line = line.rstrip()
    (szoveg,hosszStr) = line.split(':')
    hossz=float(hosszStr)
    sum+=hossz
print(f"Osszeg: {sum}")


#MEGSZÁMLÁLÁS
megszam=0
for line in lines:
    line = line.strip()
    (szoveg,hosszStr) = line.split(':')
    hossz=float(hosszStr)
    if hossz>1:
        megszam+=1
print(f"1km-nel hosszabb utak: {megszam}")

#ELDONTES
i=0
count = 0
ker = 0.5
hosszList = []
for line in lines:
    line = line.strip()
    (szoveg,hosszStr) = line.split(':')
    hossz=float(hosszStr)
    hosszList.append(hossz)
    count+=1
while i<count and hosszList[i]!=ker:
    i+=1
if i<count:
    print('van')
else:
    print('nincs')

    