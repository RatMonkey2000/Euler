from math import sqrt
k=5
numPrime=500000
primes=[2,3]
while k<numPrime:
    isPrime=True
    j=0
    while j<len(primes) and isPrime and primes[j]<=sqrt(k):
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

def percPrime(diagonalsK):
    j=0
    numPrime=0
    while j<len(diagonalsK):
        if prime(diagonalsK[j]):
            numPrime+=1
        j+=1
    return(round(numPrime/len(diagonalsK)*100))



def addLayer(diagonalJ):
    j=0
    x=int(sqrt(diagonalJ[-1])+1)
    while j<4:
        diagonalJ.append(diagonalJ[-1]+x)
        j+=1
    return diagonalJ


diagonal=[1]
num=1
solved=False
while not solved:
    num+=2
    diagonal=addLayer(diagonal)
    m=percPrime(diagonal)
    print(m)
    if m<10:
        print(num)
        solved=True