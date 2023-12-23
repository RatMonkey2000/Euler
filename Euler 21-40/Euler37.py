primes=[2]
num=3
i=0
while num<2000001:
	if num%200000==0:
		print(int(num/200000))
	i=0
	works=True 
	while i<len(primes) and works:
		if num%primes[i]==0:
			works=False
		i+=1
	if works:
		primes.append(num)
	num+=1

def tPrimeRTrue(number):
	numberS=str(int(number))
	while len(numberS)>1:
		numberI=int(numberS)
		numberS=str(numberI)[1:]
		if numberS[0]=='0':
			numberS=numberS[1:]
		if numberS[0]=='0':
			numberS=numberS[1:]
		if numberS[0]=='0':
			numberS=numberS[1:]
		if numberS[0]=='0':
			numberS=numberS[1:]
		if numberS[0]=='0':
			numberS=numberS[1:]
		if numberS[0]=='0':
			numberS=numberS[1:]
		if not int(numberS) in primes:
			return False
	if int(numberS) in primes:
		return True
	return False

def tPrimeLTrue(number):
	numberI=int(number)
	while len(str(numberI))>1:
		numberI=int(numberI)
		numberI=(numberI-(numberI%10))/10
		if numberI==0:
			return True
		if not numberI in primes:
			return False
	return True
Sum=0
numI=4
numbs=0
#print(tPrimeLTrue(2711))
while numbs<12:
	if tPrimeRTrue(primes[numI]) and tPrimeLTrue(primes[numI]):
		Sum+=prime[numI]
		numbs+=1
	numI+=1
print(Sum)