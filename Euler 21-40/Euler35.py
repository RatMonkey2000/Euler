primes=[2]
num=3
i=0
while num<1000001:
	if num%100000==0:
		print(num)
	i=0
	works=True
	while i<len(primes) and works:
		if num%primes[i]==0:
			works=False
		i+=1
	if works:
		primes.append(num)
	num+=1
def cirPrime(num):
	j=0
	num=int(num)
	works=True
	while j<len(str(num))-1 and works:
		a=num%10
		b=num-a
		c=b/10
		c=int(c)
		d=c+a*10**(len(str(num))-1)
		if not d in primes:
			return False
		num=d
		j+=1
	return True
k=0
Sum=0
while k<len(primes):
	if cirPrime(primes[k]):
		Sum+=1
	k+=1
print(Sum)