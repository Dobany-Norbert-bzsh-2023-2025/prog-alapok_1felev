int1= 1
float1 = 3.14
string1 ="asd"
bool1= True
bool2=False
bool3=int1>float1
print(int1,float1,string1,bool1,bool2,bool3)
print("------------------------")

print(*string1)#beture bontas
print("------------------------")

print(*string1,sep=",",end="-> end hasznalattal nincs sortores ->")
print(string1)
print("------------------------")

print(type(int1)) #class int -> type valtozo -> tipus/class meghatarozas -> print-el lathato
print(type(float1))
print("------------------------")

print(type(int1)==(float1))#"kompatibilitas"
print("------------------------")

print(int(float1))#tipus konverzio
print("------------------------")




