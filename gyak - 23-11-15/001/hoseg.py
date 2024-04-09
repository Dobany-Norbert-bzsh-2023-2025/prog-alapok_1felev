#Dobany Norbert 2023-11-15
print("Dobany Norbert 2023-11-15")

def ho_vizsgal(ho):
            if ho>=0:
                return False
            else:
                return True
ho=""
while ho!="vege":
        ho=input("Hő: ")
        if ho!="vege":
            ho=float(ho)
            if ho_vizsgal(ho)==False:
                print("Nem volt fagy")
            else:
                print("Fagy volt")    


        