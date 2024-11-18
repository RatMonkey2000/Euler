from itertools import combinations
from math import sqrt
k=5
numPrime=100000
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

def prime(numK):
    if numK in primes:
        return True
    return False

def replacePos(numJ,j):
    numCounter=0
    numJ=str(numJ)
    i=0
    while i<10:
        k=0
        numJChange=numJ
        while k<len(j):
            numJChange = numJChange[:int(j[k])] + str(i) + numJChange[int(j[k])+1:]
            k+=1
        if prime(int(numJChange)):
            numCounter+=1
        i+=1
    if numCounter==8:
        return True
    return False

def allReplacePos(numP):
    p=0
    permOptions=[]
    while p<len(str(numP)):
        permOptions.append(p)
        p+=1
    p=1
    while p<len(str(numP))+1:
        perm=list(combinations(permOptions,p))
        perm=[list(ele) for ele in perm]
        m=0
        while m<len(perm):
            if replacePos(numP,perm[m]):
                return True
            m+=1
        p+=1
    return False


num=1
while num<len(primes):
    if allReplacePos(num):
        print(num)
        break
    num+=1