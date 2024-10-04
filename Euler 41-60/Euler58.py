k=5
primes=[2,3]
while k<100000:
    isPrime=True
    j=0
    while j<len(primes) and isPrime:
        if k%primes[j]==0:
            isPrime=False
        j+=1
    if isPrime:
        primes.append(k)
    k+=2

def prime(numK):
    if numK in primes:
        return True
    return False

