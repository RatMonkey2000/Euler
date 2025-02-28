from math import sqrt
k=5
numPrime=10000000
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

fraction=[1,1]
def addLayer(x,frac):
    frac[1]+=4
    num1=4*x**2-10*x+7
    num2=4*x**2-10*x+7+x*2-2
    num3=4*x**2-10*x+7+x*4-4
    num4=4*x**2-10*x+7+x*6-6
    if prime(num1):
        frac[0]+=1
    if prime(num2):
        frac[0]+=1
    if prime(num3):
        frac[0]+=1
    if prime(num4):
        frac[0]+=1
    return frac

n=2
done=False
while not done:
    fraction=addLayer(n,fraction)
    print((100*fraction[0])//fraction[1])
    if (100*fraction[0])//fraction[1]<10:
        print(2*n-1)
        done=True
    n+=1