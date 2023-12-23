a=2
b=2
add=0
nums=[]
while a<101:
	b=2
	while b<101:
		if not a**b in nums:
			add+=1
			nums.append(a**b)
		b+=1
	a+=1
print(add)