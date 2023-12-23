num=2
origNum=2
length=0
highestLen=1
highestNum=2
while origNum<1000001:
    num=origNum
    length=0
    while num!=1:
        if num%2==0:
            num/=2
        else:
            num*=3
            num+=1
        length+=1
    if length>highestLen:
        highestLen=length
        highestNum=origNum
    origNum+=1
print(highestNum)
