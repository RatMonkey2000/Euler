num=600851475143
factor=3
while factor<600851475143/3+1:
        if num%factor==0:
                num/=factor
                if num==1:
                        num*=factor
                        break
        else:
                factor+=1
print(num)
