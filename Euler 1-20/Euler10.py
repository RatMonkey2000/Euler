primes=[2,3]
sumP=5
prime=5
i=0
works=True
while prime<2000000:
    i=0
    works=True
    while i<len(primes):
        if prime%primes[i]:
            i+=1
        else:
            works=False
            break
    if works==True:
        sumP+=prime
        primes.append(prime)
        print(prime)
    prime+=2
print(sumP)
