primes=[2,3]
prime=5
i=0
works=True
while len(primes)<10001:
    works=True
    while i<len(primes):
        if prime%primes[i]!=0:
            i+=1
        else:
            works=False
            break
    if works==True:
        primes.append(prime)
    i=0
    prime+=2
print(primes[-1])
