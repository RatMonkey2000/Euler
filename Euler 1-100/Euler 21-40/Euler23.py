def abundantTrue(numI):
	SumI=1
	i=2
	while i<numI/2+1:
		if numI%i==0:
			SumI+=i
		i+=1
	if SumI>numI:
		return(True)
	else:
		return(False)
num=1
abundant=[]
while num<28124:
	if abundantTrue(num):
		abundant.append(num)
	num+=1
num=1
i=0
print(abundant)
Sum=0
while num<28124:
	if num%1000==0:
		print(num)
	i=0
	works=False
	while i<len(abundant) and works==False and abundant[i]<num:
		if abundantTrue(num-abundant[i]):
			works=True
		i+=1
	if works==False:
		Sum+=num
	num+=1
print(Sum)
