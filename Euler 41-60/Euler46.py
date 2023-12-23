import math
limit=300000
primes=[2]
compositesOdd=[]
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
    else:
        if numJ%2==1:
            compositesOdd.append(numJ)
    numJ+=2

print("Yes")
#print(compositesOdd)

def prime(numI):
    if numI in primes:
        return True
    return False

def conjTrue(numK,k):
    while k<len(primes) and primes[k]<numK:
        if math.sqrt((num-primes[k])/2)%1==0:
            return True
        k+=1
    return False

works=False
j=1

while j<len(compositesOdd):
    works=False  
    num=compositesOdd[j]
    #print(num)
    i=0

    if j%(limit/10)==0:
        print(j)

    works=conjTrue(num,i)

    if works==False:
        print(num)
        break
    j+=1