import math
counter=[]
x=0
while x<1000:
	counter.append(0)
	x+=1	
a=3
b=4
while a<1000:
        b=a+1
        while b<1000:
                c=math.sqrt(a**2+b**2)
                if c%1==0 and (a+b+c)<=1000:
                        counter[int(a+b+c-1)]+=1
                b+=1
        a+=1
maxi=max(counter)
print(counter.index(maxi)+1)
