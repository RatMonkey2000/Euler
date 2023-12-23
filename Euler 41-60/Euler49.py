import math
from itertools import permutations
limit=10020
primes=[2]
numJ=3
i=0

while numJ<limit:
    i=0
    works=True
    while i<len(primes) and works:
        if numJ%primes[i]==0:
            works=False
        i+=1
    if works:
        primes.append(numJ)
    numJ+=2

def prime(numK):
    if numK in primes:
        return True
    return False

i=168
done=False
while i<len(primes) and not done:
    perm=[''.join(i) for i in permutations(str(primes[i]))]
    perm = list(dict.fromkeys(perm))

    j=1
    while j<len(perm) and not done:
        if prime(int(perm[j])-int(perm[0])+int(perm[j])) and prime(int(perm[j])) and str(int(perm[j])-int(perm[0])+int(perm[j])) in perm and not perm[0]=='1487':
            print(perm[0]+perm[j]+str(int(perm[j])-int(perm[0])+int(perm[j])))
            print(j)
            print(perm)
            done=True
        j+=1
    i+=1