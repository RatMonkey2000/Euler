from math import sqrt
k=5
primes=[2,3]
while k<1000000:
    isPrime=True
    j=0
    while j<len(primes) and isPrime and primes[j]<sqrt(k):
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

def perPrime(diagonals):
    l=0
    numPrime=0
    while l<len(diagonals):
        if prime(diagonals[l]):
            numPrime+=1
        l+=1
    return(numPrime/len(diagonals)*100)
    

def dia(limit):
    limit=(limit-1)/2
    diagonals=[1]
    numJ=1
    m=2
    x=0
    n=0
    while x<limit:
        n=0
        while n<4:
            numJ+=m
            diagonals.append(numJ)
            n+=1
        m+=2
        x+=1
    return(perPrime(diagonals))

num=3
solved=False
while not solved:
    print(num)
    x=round(dia(num))
    print(dia(num))
    if dia(num)<10:
        print(num)
        solved=True
    num+=2