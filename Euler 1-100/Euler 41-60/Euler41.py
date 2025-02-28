import itertools
def isPrime(n):
        i=2
        while i<n/2+1:
                if n%i==0:
                        return False
                i+=1
        return True
notGot=True
num='1234567'
numList=list(map("".join, itertools.permutations(num)))
i=len(numList)-1
while i>-1 and notGot:
        if isPrime(int(numList[i])):
                print(int(numList[i]))
                notGot=False
        i-=1
num='1234'
numList=list(map("".join, itertools.permutations(num)))
i=len(numList)-1
while i>-1 and notGot:
        if isPrime(int(numList[i])):
                print(int(numList[i]))
                notGot=False
        i-=1
