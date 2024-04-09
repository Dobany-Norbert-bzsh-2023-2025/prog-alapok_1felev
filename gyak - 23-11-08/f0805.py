import statistics
txt=open('dolgozok.txt','r',encoding='utf-8')
lines = txt.readlines()
fizetes=[]
for i in lines:
   print(i,end='\n')
   fizetes.append(int(i.split(':')[4]))
print('osszeg: {}'.format(sum(fizetes)))
print('atlag: {}'.format(statistics.mean(fizetes)))  

"""
alternativa

for i in line:
   (az, nev, tel, cim, fiz, szul) = line.split(':')
   print(fiz)        
"""