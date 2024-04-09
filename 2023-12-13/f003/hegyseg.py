# Nagy János, 15m, 2023-12-12

from hegy import Hegy

class App:
    def __init__(self):
        self.filename = "f003/hegyek.txt"
        self.hegyLista = []
    
    def readfile(self):
        fp = open(self.filename, "r", encoding="utf-8")
        lines = fp.readlines()[1:]
        fp.close()
        
        for line in lines:
            line = line.rstrip()
            (az, hegyseg, nev, csucs, magassag, allat) = line.split(",")
            hegy = Hegy(az, hegyseg, nev, csucs, magassag, allat)
            self.hegyLista.append(hegy)
    
    # Hány alpok hegy van?
    def szamol_alpok(self):
        count = 0
        for hegy in self.hegyLista:
            if hegy.nev == "Alpok":
                count += 1
        print("Alpok darabszám:", count)
    
    
    # A legalacsonyabb csúcs minden adata
    def min_hegy_datas(self):
        minHegy = self.hegyLista[0]
        for hegy in self.hegyLista:
            if hegy.magassag < minHegy.magassag:
                minHegy = hegy
        
        print("Legkisebb csúcs:")
        print("%s : %s : %s : %s : %s : %s" % 
              (minHegy.az, 
              minHegy.hegyseg, 
              minHegy.nev, 
              minHegy.csucs, 
              minHegy.magassag,
              minHegy.allat
              ))
        
    # 4000 méternél kisebb neve, 
    # hegysége és magassága alacsony.txt fájlba
    # kettősponttal tagolva
    def ki_alacsony(self):
        fp = open("f003/alacsony.txt", "w", encoding="utf-8")
        for hegy in self.hegyLista:
            if float(hegy.magassag) < 4000:
                fp.write(hegy.nev)
                fp.write(";")
                fp.write(hegy.hegyseg)
                fp.write(";")
                fp.write(hegy.magassag)
                fp.write(":")
        fp.close()
        

    # Hány hegy jellemzője a havasi sas?
    def szamol_havasi_sas(self):
        count = 0
        for hegy in self.hegyLista:
            if hegy.allat=="Havasi sas":
                count+=1
        print(f"{count} hegy jellemező állata a havasi sas")

app = App()

app.__init__()
app.readfile()
app.szamol_alpok()
app.min_hegy_datas()
app.ki_alacsony()
app.szamol_havasi_sas()

        