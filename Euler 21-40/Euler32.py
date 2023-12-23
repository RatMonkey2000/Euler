def panTrue(num):
	i=0
	numL=[]
	while i<len(str(num)):
		numL.append(str(num)[i])
		i+=1
	i=1
	while i<=len(numL):
		if not str(i) in numL:
			return(False)
		i+=1
	return(True)

first=1
second=1
answers=[]
while first<10000:
	if first%1000==0:
		print(first)
	second=first+1
	while second<10000:
		if len(str(first)+str(second)+str(first*second))==9 and panTrue(str(first)+str(second)+str(first*second)):
			if not first*second in answers:
				answers.append(first*second)
		second+=1
	first+=1
print(sum(answers))