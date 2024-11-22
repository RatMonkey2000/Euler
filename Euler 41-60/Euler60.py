from math import sqrt
k=5
numPrime=1000000
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

def prime(numK):
    if numK in primes:
        return True
    return False

def testPrimes(setPrimes):
    i=0
    works=True
    while i<5 and works:
        j=i+1
        while j<5 and works:
            if not prime(int(str(setPrimes[i])+str(setPrimes[j]))) and not prime(int(str(setPrimes[j])+str(setPrimes[i]))):
                works=False
            j+=1
        i+=1
    return works

def whatSum(setPrimes):
    i=0
    Sum=0
    while i<5:
        Sum+=setPrimes[i]
        i+=1
    return Sum



a=0
done=False
while a<len(primes) and not done:
    print(a)
    b=a+1
    while b<len(primes) and not done:
        print(b)
        c=b+1
        while c<len(primes) and not done:
            print(c)
            d=c+1
            while d<len(primes)and not done:
                print(d)
                e=d+1
                while e<len(primes) and not done:
                    if testPrimes([primes[a],primes[b],primes[c],primes[d],primes[e]]):
                        print([primes[a],primes[b],primes[c],primes[d],primes[e]])
                        done=True
                    e+=1
                d+=1
            c+=1
        b+=1
    a+=1