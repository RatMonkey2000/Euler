fib=[1,2]
while (fib[-1]+fib[-2])<4000001:
	fib.append(fib[-1]+fib[-2])
i=0
sum=0
while i<len(fib):
	if fib[i]%2==0:
		sum+=fib[i]
	i+=1
print(sum)