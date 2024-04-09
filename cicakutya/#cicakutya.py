#HÁZI FELADAT FEJLESZTÉS JÓL FUNKCIÓNÁLÓ PROGRAMRA
#cicakutya
#két osztály: Cica és Kutya az a kérdés, hogy éhes-e
#Ha éhes akkor adunk enni HA nem éhes akkor alszik
class Cica:
    def __init__(self, nev, kapotte):
        self.nev=nev
        self.kapotte=kapotte
    def cicacheck(self):
        if self.kapotte==False:
            print(f"{self.nev}-nak/nek enni kell adni")
        else:
            print(f"{self.nev} most alszik")
           
class Kutya:
    def __init__(self, nev, kapotte):
        self.nev=nev
        self.kapotte=kapotte
    def __init__(self, nev, kapotte):
        self.nev=nev
        self.kapotte=kapotte
    def kutyacheck(self):
        if self.kapotte==False:
            print(f"{self.nev}-nak/nek enni kell adni")
        else:
            print(f"{self.nev} most alszik")
      
#cica és Ktya létrehozása:
cicanev=input("Mi a cica neve?:")
cicaehseg=bool(input(f"Kapott enni {cicanev}? True/False: "))
cica1=Cica(cicanev,cicaehseg)
cica1.cicacheck()

kutyanev=input("Mi a kutyus neve?:")
kutyaehseg=bool(input(f"Kapott enni {kutyanev}? True/False: "))
kutya1=Kutya(kutyanev,kutyaehseg)
kutya1.kutyacheck()  

   
        
        
        
    


