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

def perPrime():
    l=0
    numPrime=0
    while l<len(diagonals):
        if prime(diagonals[l]):
            numPrime+=1
        l+=1

def Dia(limit):
    diagonals=[1]
    n=0
    x=0
    m=2
    numK=3
    while x<limit:
        n=1
        while n<4:
            diagonals.append(numK)
            numK+=m
            n+=1
        m+=2
        x+=1
        perPrime()
print("Goose")