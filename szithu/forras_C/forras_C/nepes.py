#Dobany szofti/1/n 2024-01-03
print("Dobany szofti/1/n 2024-01-03")

def megfelel(self):
    if self<500:
        return True
    else:
        return False

nepes = 1
while nepes!=0:
    nepes=int(input("nepsuruseg?:"))
    if nepes!=0:
        if megfelel(nepes):
            print("megfelel")
        else:
            print("tul sok")
        