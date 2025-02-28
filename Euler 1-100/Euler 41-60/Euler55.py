def palendromic(numK):
    numK=str(numK)
    k=0
    while k<len(numK)/2:
        if numK[k]!=numK[0-k-1]:
            return False
        k+=1
    return True


def flipnadd(numJ):
    numJ=str(numJ)
    j=0
    numJR=""
    while j<len(numJ):
        numJR=numJ[j]+numJR
        j+=1
    numJR=int(numJR)+int(numJ)
    return numJR
    
def lychrel(numI):
    i=0
    while i<50:
        numI=flipnadd(numI)
        if palendromic(numI):
            return False
        i+=1
    return True



num=1
totNum=0
while num<10001:
    if lychrel(num):
        totNum+=1
    num+=1
print(totNum)