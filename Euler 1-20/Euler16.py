num=2**1000
length=len(str(num))
i=0
sumNum=0
while i<length:
    sumNum+=int(str(num)[i])
    i+=1
print(sumNum)
