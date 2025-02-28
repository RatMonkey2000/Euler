def fact(num):
	i=0
	product=1
	while i<num:
		product*=num-i
		i+=1
	return product
def check(num):
	j=0
	Sum2=0
	while j<len(str(num)):
		Sum2+=fact(int(str(num)[j]))
		j+=1
	if Sum2==num:
		return True
	else:
		return False
numD=10
Sum=0
while numD<1000001:
	if check(numD):
		Sum+=numD
	numD+=1
print(Sum)