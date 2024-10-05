k=5
primes=[2,3]
while k<10000:
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

print("Done")

def perPrime():
    diagonals=[]
    l=0
    numPrime=0
    while l<len(diagonals):
        if prime(diagonals[l]):
            numPrime+=1
        l+=1
    

def Dia(limit):
    diagonals=[]
    numJ=1
    m=2
    x=0
    n=0
    while x<limit:
        n=0
        while n<4:
            diagonals.append(numJ)
            numJ+=m
            n+=1
            print(m)
        m+=2
        x+=1
    print(diagonals)
Dia(2)