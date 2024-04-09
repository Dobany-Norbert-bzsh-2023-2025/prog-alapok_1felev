#Dobany szofti/1/n 2024-01-03
print("Dobany szofti/1/n 2024-01-03")

from telepules import Telepules

class Telep:
    def __init__(self):
        self.fajlnev = 'telepulesek.txt'
        self.telepulesLista = []
    
    # Fájl beolvasása
    def fajl_baolvas(self):
        fp = open(self.fajlnev, 'r', encoding='utf-8')
        lines = fp.readlines()
        fp.close()
        for line in lines[1:]:
            line = line.rstrip()
            (az, nev, megye, nepesseg, terulet, nepsuruseg) = line.split(';')
            telepules = Telepules(az, nev, megye, nepesseg, terulet, nepsuruseg)
            self.telepulesLista.append(telepules)
    
    # Írassa ki a Pest megyei települések neveit
    def kiir_pest_telepules(self):
        print('települések---')
        for telepules in self.telepulesLista:
            if telepules.megye == 'Pest':
                print(telepules.nev)
    
    # Jelenítse meg azokat a településeket,
    # amelyek népessége több mint 150 ezer.
    # Írassa ki a nevet és a népességet
    def kiir_nagy_nepesseg(self):
        print('---Nagy népesség---')
        for telepules in self.telepulesLista:
            if int(telepules.nepesseg) > 150000 :
                print(telepules.nev)
    
    # Jelenítse meg azokat a településeket,
    # ahol népsűrűség nagyobb mint 1000
    # Írassa ki a nevet és a népsűrűséget
    def kiir_nagy_nepsuruseg(self):
        for telepules in self.telepulesLista:
            if float(telepules.nepsuruseg) > 1000 :
                print(telepules.nev,telepules.nepsuruseg)

    # Írja fájlba a 300 főnél kisebb népsűrűségű 
    # települések neveit és a népsűrűséget
    # és a megyét.
    # A fájl neve kissur.txt legyen.
    # Az oszlopokat kettősponttal tagolja
    def kiir_kis_nepsuruseg(self):
        print('---Kis népsűrűség fájlba---')
        fp = open('kissur.txt', 'w', encoding='utf-8')
        for telepules in self.telepulesLista:
            if float(telepules.nepsuruseg) < 300 :
                print(telepules.nev, telepules.nepsuruseg)
                fp.write(telepules.nev)
                fp.write(':')
                fp.write(telepules.nepsuruseg)
                fp.write('\n')
        fp.close()        

    # --- PLUSZ FELADATOK gyakorláshoz ---

    # Plussz feladat
    # Jelenítse meg azoknak a településeknek az adatati
    # amelyek területe nagyobb mint 400 négyzetkilométer
    # Jelenjen meg település neve és területe
    def kiir_nagy_terulet(self):
        print("---Nagy terület---")
        for telepules in self.telepulesLista:
            if float(telepules.terulet) > 400:
                print(telepules.nev,telepules.terulet)

    # Plussz feladat
    # Jelenítse meg a legkisebb terület település
    # összes adatát
    def kiir_legkisebb_teruletu(self):
        print("---Legkisebb terület---")
        min = float(self.telepulesLista[0].terulet)
        for telepules in self.telepulesLista:
            if float(telepules.terulet)<min:
                min = float(telepules.terulet)
        for telepules in self.telepulesLista:
            if float(telepules.terulet) == min:
                        print(telepules.az,telepules.megye,telepules.nepesseg,telepules.nepsuruseg,telepules.nev,telepules.terulet)
                        
    def kiir_legkisebb_teruletu(self):
        print("---Legkisebb terület---")
        min = self.telepulesLista[0] 
        for telepules in self.telepulesLista:
            if float(telepules.terulet)<float(min.terulet):
                min = telepules
        print(min.megye,min.nepesseg,min.nepsuruseg,min.nev,min.terulet)        
            

    # Plussz feladat
    # Jelenítse meg a legnagyobb népsűrűségű település
    # nevét és népsűrűségét
    def kiir_legnagyobb_nepsuruseg(self):
        print("---Legnagyobb népsűrűség---")
        max = float(self.telepulesLista[0].nepsuruseg)
        for telepules in self.telepulesLista:
            if float(telepules.nepsuruseg)>max:
                max = float(telepules.nepsuruseg)
        for telepules in self.telepulesLista:
            if float(telepules.nepsuruseg) == max:
                        print(telepules.nepsuruseg,telepules.nev)        
            

telep = Telep()
telep.fajl_baolvas()
telep.kiir_pest_telepules()
telep.kiir_nagy_nepesseg()
telep.kiir_nagy_nepsuruseg()
telep.kiir_kis_nepsuruseg()
telep.kiir_nagy_terulet()
telep.kiir_legkisebb_teruletu()
telep.kiir_legnagyobb_nepsuruseg()   