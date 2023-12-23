limit=1000000
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

greatestSum=0
longest=0
start=0
while start<len(primes):
    i=start
    Sum=0
    counter=0
    while Sum<limit and i<len(primes):
        Sum+=primes[i]
        i+=1
        counter+=1
        if counter>longest and prime(Sum):
            greatestSum=Sum
            longest=counter
    start+=1
print(greatestSum)