class Macska:
    def __init__(self,nev,ehes):
        self.nev=nev
        self.ehes=False
    def etetes(self):
        self.ehes=True
        print(f"{self.nev}-nek enni kell adni")
    def alvas(self):
        self.ehes=False
        print(f"{self.nev} most alszik")
        
class Kutya :
    def __init__(self,nev,ehes):
        self.nev=nev
        self.ehes=False
    def etetes(self):
        self.ehes=True
        print(f"{self.nev}-nek enni kell adni")
    def alvas(self):
        self.ehes=False
        print(f"{self.nev} most alszik")