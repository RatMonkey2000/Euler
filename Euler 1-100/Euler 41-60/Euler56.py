def digitSum(numJ):
    Sum=0
    j=0
    while j<len(str(numJ)):
        Sum+=int(str(numJ)[j])
        j+=1
    return Sum



a=1
b=1
maxSum=0
while a<100:
    b=1
    while b<100:
        if digitSum(a**b)>maxSum:
            maxSum=digitSum(a**b)
        b+=1
    a+=1

print(maxSum)