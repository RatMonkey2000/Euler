def palTrue(num):
	if len(str(num))%2==0:
		i=0
		while i<=len(str(num))/2:
			j=-i-1
			if str(num)[i]!=str(num)[j]:
				return False
			i+=1
	else:
		i=0
		while i<len(str(num))/2:
			j=-i-1
			if str(num)[i]!=str(num)[j]:
				return False
			i+=1
	return True
def bothPal(num):
	if palTrue(num) and palTrue(int((str(bin(num))[2:]))):
		return True
	return False
numI=1
Sum=0
while numI<1000000:
	if bothPal(numI):
		Sum+=numI
		print(numI)
	numI+=1
print(Sum)