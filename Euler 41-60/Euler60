from math import sqrt
k=5
numPrime=2000000
primes=[2,3]
while k<numPrime:
    if (k-1)%(numPrime/10)==0:
        print(int((k-1)/(numPrime/10)))
    isPrime=True
    j=0
    while j<len(primes) and isPrime and primes[j]<sqrt(k):
        if k%primes[j]==0:
            isPrime=False
        j+=1
    if isPrime:
        primes.append(k)
    k+=2


def prime(numP):
    if numP in primes:
        return True
    return False


def ifWorks(set):
    i=0
    works=True
    while i<4 and works:
        j=i+1
        while j<4 and works:
            if not prime(int(str(primes[set[i]])+str(primes[set[j]]))) or not prime(int(str(primes[set[j]])+str(primes[set[i]]))):
                works=False
            j+=1
        i+=1
    return works


