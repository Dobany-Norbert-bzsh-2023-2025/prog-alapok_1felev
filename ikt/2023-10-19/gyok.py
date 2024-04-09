"""

num=int
i=1
sq=1
while True:
    if sq*sq==num:
        print(f"a {num} negyzetgyoke: {sq}")
        break
    else:
        if sq*sq<17:
            #sq=sq+i
            sq+=i
        else:
            sq-=i
            if i>0.000001:
                i/=10
                sq+=i
            else:
                print(f"a {num} negyzetgyoke: {sq}")
                break    
        """
import math
log=True
ans = ""

while log:
    num=int(input("give me a number"))
    if num<=0:
        print("cant use this number")
    else:    
        print(math.sqrt(num))
    ans = input("again? y/n")
    if ans == "y":
        continue
    else:
        break


        
            
 
