prev=1
add=2
Sum=1
count=1
while count<=500:
	Sum+=prev+add
	Sum+=prev+add*2
	Sum+=prev+add*3
	Sum+=prev+add*4
	prev+=add*4
	add+=2
	count+=1
print(Sum)