import math
def reciprical(num):
	i=1
	
	answer=[0]
	remain=[1]
	NotRepeated=True
	while NotRepeated:
		j=0
		while j<len(remain)-1 and NotRepeated:
			if remain[-1]==remain[j]:
				NotRepeated=False
			j+=1
		if NotRepeated:
			answer.append(math.floor(remain[-1]*10/num))
			remain.append(remain[-1]*10-answer[-1]*num)
		i+=1
	answer.pop(0)
	return(len(answer)-j+1)

d=999
longest=0
while d>1:
        if reciprical(d)>longest:
                longest=reciprical(d)
                longestN=d
        d-=1
print(longestN)  
