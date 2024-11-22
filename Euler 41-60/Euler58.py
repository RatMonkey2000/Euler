from math import sqrt
k=5
numPrime=50
primes=[2,3]
while k<numPrime:
    if (k-1)%(numPrime/10)==0:
        print(int((k-1)/(numPrime/10)))
    isPrime=True
    j=0
    while j<len(primes) and isPrime and primes[j]<=sqrt(k):
        if k%primes[j]==0:
            isPrime=False
        j+=1
    if isPrime:
        primes.append(k)
    k+=2

print(primes)
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
    return(numPrime/len(diagonalsK)*100)

def addLayer():
    j=0
    x=sqrt(diagonal[-1])+1
    while j<4:
        diagonal.append(diagonal[-1]+x)
        j+=1

diagonal=[1]
num=1
solved=False
while not solved:
    num+=2
    addLayer()
    print(percPrime(diagonal))
    if percPrime(diagonal)<10:
        print(num)
        solved=True