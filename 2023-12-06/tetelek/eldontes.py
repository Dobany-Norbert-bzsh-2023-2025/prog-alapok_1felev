szam = [1,2,3,4,5,6,7]
n=len(szam)
ker = 35

i=0
while i<n and szam[i]!=ker:
    i+=1
    
if i<n:
    print('van')
else:
    print('nincs')
