Sum=0
num=1
while num<1001:
    Sum+=num**num
    num+=1
print(Sum%10000000000)