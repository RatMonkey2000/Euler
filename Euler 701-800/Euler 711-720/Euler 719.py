from math import sqrt
num=101
Sum=41333

def listWorks(listi):
    i=0
    sumNum=0
    while i<len(listi):
        sumNum+=int(listi[i])
        i+=1
    return sumNum

def nextPerm(listi):
    i=0
    while i<len(listi):
        if len(listi[i])!=1:
            if listi[i+1]==None:
                listi[i+1]=listi[i][-1]
            else:
                listi[i+1]+=listi[i][-1]
            return listi
        else:
            i+=1
    return False

def isnatural(num):
    i=0
    splits=[]
    while i<len(str(num)):
        splits.append(None)
        i+=1
    splits.append(str(num))
    while not listWorks(listi):
        listi=nextPerm(listi)
    if listi==False:
        return False
    else:
        return True

print(isnatural(7))