from math import sqrt
import sympy
k=5
primes=[2,3]
while k<10000000:
    isPrime=True
    j=0
    while j<len(primes) and isPrime and primes[j]<sqrt(k):
        if k%primes[j]==0:
            isPrime=False
        j+=1
    if isPrime:
        primes.append(k)
    k+=2

print("Goose")

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
    

def dia(diagonals):
    numJ=diagonals[-1]
    m=len(diagonals)/2+1.5
    x=0
    n=0
    while n<4:
        numJ+=m
        diagonals.append(numJ)
        n+=1
    return(perPrime(diagonals))

num=3
solved=False
diagonals=[1]
while not solved:
    if dia(diagonals)<10:
        solved=True