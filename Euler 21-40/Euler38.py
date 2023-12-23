def pan9True(num):
	pan = True
	I=1
	numS=str(num)
	while I<10 and pan:
		if not str(I) in numS:
			pan=False
		I+=1
	return pan
def conk(seed):
	conkNum=''
	n=1
	while len(conkNum)<9:
		conkNum+=str(n*seed)
		n+=1
	return int(conkNum)
biggest=192384576
for integ in range(193,9877):
	if pan9True(conk(integ)) and len(str(conk(integ)))==9:
		if conk(integ)>biggest:
			biggest=conk(integ)
print(biggest)
	
	
		