import random
def Veletlen():
    print("Véletlen:")
    global a
    global b
    global c
    while True:
        pontok =[]
        for i in range(0,3):
            x = random.randint(-1000,1000)
            y = random.randint(-1000,1000)
            pontok.append({'x':x,'y':y})
        a = Tavolsag(pontok[0]['x'],pontok[0]['y'],pontok[1]['x'],pontok[1]['y'])    
        b = Tavolsag(pontok[1]['x'],pontok[1]['y'],pontok[2]['x'],pontok[2]['y'])  
        c = Tavolsag(pontok[2]['x'],pontok[2]['y'],pontok[0]['x'],pontok[0]['y'])
        if a+b>c and a+c>b and b+c>a:
            break
def Koordinatak():
    print("Koordináták:")
def Oldalak(a,b,c):
    print("Oldalak")
    while True:
        while True:
            try:
                a=int(input("a: "))
                break
            except:
                continue
        while True:    
            try:
                b=int(input("b: "))
                break
            except:
                continue
        while True:    
            try:
                c=int(input("c: "))
                break
            except:
                continue
        
            
def Kerulet(a,b,c):
    return a+b+c
def Terulet():
    pass
    



if __name__=="__main__":
    print("Válasszon!")
    print("\t1.Véletlen csúcsok")
    print("\t2.Csúcs koordináták megadása")
    print("\t3.Oldalak megadása")
    while True:
        try:
            szam=int(input("Melyik legyen?:"))
        except:
            print("Nem megfelelő válasz! Adj meg újat!")
            continue
        if szam==1 or szam==2 or szam==3:
            match szam:
                case 1:
                    Veletlen()
                    break
                case 2:
                    Koordinatak()
                    break
                case 3:
                    Oldalak()
                    break
                case _:
                    pass
            
        else:
            print("Nem megfelelő válasz! Adj meg újat!")