#Dobany Norbert 2023-11-07
import statistics

print("Dobany 2023-11-07 \nA program megvizsgálja három tehenészeti telephely egyhónapos tejhozamát és eldönti, hogy kell -e a hozam növelése érdekében több tehenetvásárolni. \nCsak 500 liter tejhozam átlag alatt kell tehenet vásárolni!!!")

t1=452.35
t2=628.45    
t3=553
tlist=[t1,t2,t3]

atlag=statistics.mean(tlist)
#print(atlag)


if atlag<500:
    print("\nAz átlagtejhozam: {} liter,tehenet kell vásárolni.".format(atlag))
else:
    print("\nAz átlagtejhozam {} liter, nem kell tehenet vásárolni. ".format(atlag))





