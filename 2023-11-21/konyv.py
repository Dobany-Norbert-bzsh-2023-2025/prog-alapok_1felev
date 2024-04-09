class Konyv:
    def __init__(self, cim, szerzo):
        self.cim=cim
        self.szerzo=szerzo

konyv1=Konyv("Cím1","Szerző1")
konyv2=Konyv("Cím2","Szerző2")

print(konyv1.cim,konyv1.szerzo)
