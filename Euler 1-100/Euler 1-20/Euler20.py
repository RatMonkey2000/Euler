num=100
Sum=0
numF=1
while num>1:
    numF*=num
    num-=1
j=0
while j<len(str(numF)):
    Sum+=int(str(numF)[j])
    j+=1
print(Sum)
