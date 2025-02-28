def d(num):
    Sum=0
    i=1
    while i<num/2+1:
        if num%i==0:
            Sum+=i
        i+=1
    return(Sum)
sumA=0
numA=2
f=0
while numA<10001:
    f=d(numA)
    if numA==d(f) and numA!=f:
        sumA+=numA
    numA+=1
print(sumA)
