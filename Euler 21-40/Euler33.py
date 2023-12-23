def simple(num,den):
	numL=[str(num)[0],str(num)[1]]
	denL=[str(den)[0],str(den)[1]]
	if int(numL[1])==int(denL[0]):
		numL.pop(1)
		denL.pop(0)
	i=-1
	newNum=0
	newDen=0
	while i>=0-len(numL):
		newNum+=int(numL[i])*(-i*9-8)
		i-=1
	i=-1
	while i>=0-len(denL):
		newDen+=int(denL[i])*(-i*9-8)
		i-=1
	if newDen==0:
		return False
	if newNum/newDen!=num/den:
		return False
	else:
		if newNum*10==num:
			return False
		else:
			if len(str(newNum))==1:
				return True
			else:
				return False	
numer=10
denom=11
product=1
while numer<100:
	denom=numer+1
	while denom<100:
		if simple(numer,denom):
			product*=int(numer/denom*100)/100
			product=int(product*100)/100
		denom+=1
	numer+=1
from fractions import Fraction
print(Fraction(str(product)))