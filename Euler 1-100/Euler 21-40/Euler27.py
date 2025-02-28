primes=[2]
num=3
i=0
while num<1001:
    i=0
    works=True
    while i<len(primes) and works:
        if num%primes[i]==0:
            works=False
        i+=1
    if works:
        primes.append(num)
    num+=1
def prime(num):
    i=0
    isPrime=False
    if num in primes:
        isPrime=True
    return(isPrime)
a=-999
b=-1000
count=0
longest=0
longestProduct=0
while a<1000:
    if a%100==0:
        print(a)
    b=-1000
    while b<1001:
        count=0
        num=0
        while prime(num**2+a*num+b):
            count+=1
            num+=1
        if count>longest:
            longest=count
            longestProduct=a*b
        b+=1
    a+=1
print(longestProduct)
