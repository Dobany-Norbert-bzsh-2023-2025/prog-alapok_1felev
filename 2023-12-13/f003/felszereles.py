def magashegy(magassag):
    if magassag>2500:
        return True
    else:
        return False


valaszStr=""        
while valaszStr!="vege":
    valaszStr=input("Milyen magas a hegy? (m): ")
    if valaszStr!="vege":
        valaszInt=int(valaszStr)
        if magashegy(valaszInt)==True:
            print("oxigén ajánlott")
        else:
            print("normál körülmények")
    