from math import sqrt

def listWorks(listi):
    i=0
    sumNum=0
    while i<len(listi):
        print(listi[i])
        if listi[i]!=None and listi[i]!='00' and listi[i]!='000' and listi[i]!='0000' and listi[i]!='00000' and listi[i]!='000000':
            sumNum+=int(listi[i])
        i+=1
    return sumNum

def nextPerm(listi):
    i=0
    while i<len(listi):
        if len(listi[i])!=1:
            if listi[i+1]==None:
                listi[i+1]=listi[i][-1]
                listi[i]=listi[i][:-1]
            else:
                listi[i+1]=listi[i][-1]+listi[i+1]
                listi[i]=listi[i][:-1]
            return listi
        else:
            i+=1
    return False

def isnatural(num):
    i=1
    splits=[]
    splits.append(str(num))
    while i<len(str(num)):
        splits.append(None)
        i+=1
    done=False
    while not done:
        if listWorks(splits)==sqrt(num):
            done=True
            break
        splits=nextPerm(splits)
        if splits==False:
            break
    if done:
        print(splits)
        return True
    return False
    
"""num=101
Sum=41333
while num<1000001:
    if isnatural(num**2):
        print(num)
        Sum+=num**2
    num+=1
print(Sum)"""
print(isnatural(10000000000))