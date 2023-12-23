num='0.'
n=1
while n<1000000:
    num+=str(n)
    n+=1
num=num[2:]
product=1
i=0
while i<7:
    product*=int(num[10**i-1])
    i+=1
print(product)
