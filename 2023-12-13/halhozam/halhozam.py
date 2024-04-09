#szit.hu/int helye
f=open("halhozam.txt","w")
#while True:
#    valasz = input("Hany kg volt a halhozam?: ")
#    if valasz=="vege":
#        break
#    else:
#        valasz=int(valasz)
#    
#    if valasz>5000:
#        f.write("Megfelelő\n")
#    else:
#        f.write("Kevés\n")

valaszStr=""        
while valaszStr!="vege":
    valaszStr=input("Hany kg volt a halhozam?: ")
    if valaszStr!="vege":
        valaszInt=int(valaszStr)
        if valaszInt>5000:
            f.write(f"Megfelel - {valaszStr}\n")
        else:   
            f.write(f"Kevés - {valaszStr}\n")
f.close()  