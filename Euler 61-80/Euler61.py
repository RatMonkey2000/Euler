from math import sqrt
def isTrianglular(numJ):
    numJ=-1/2+sqrt(2*numJ+1/4)
    if numJ%1==0:
        return True
    return False

def isSquare(numJ):
    if sqrt(numJ)%1==0:
        return True
    return False

def isPentagonal(numJ):
    numJ=1/6+sqrt(2*numJ/3+1/36)
    if numJ%1==0:
        return True
    return False

def isHexagonal(numJ):
    numJ=1/4+sqrt(numJ/2+1/16)
    if numJ%1==0:
        return True
    return False

def isHeptagonal(numJ):
    numJ=3/10+sqrt(2*numJ/5+9/100)
    if numJ%1==0:
        return True
    return False

def isOctagonal(numJ):
    numJ=1/3+sqrt(numJ/3+1/9)
    if numJ%1==0:
        return True
    return False

def works(listJ)
    done=[3,4,5,6,7,8]
    i=0
    while i<6:
        if isTrianglular(listJ[i]):
            listJ.pop(i)
            done.remove(3)
        i+=1
    i=0
    while i<6:
        if isSquare(listJ[i]):
            listJ.pop(i)
            if 4 in done:
                done.remove(4)
        i+=1
    i=0
    while i<6:
        if isPentagonal(listJ[i]):
            listJ.pop(i)
            if 5 in done:
                done.remove(5)
        i+=1
    i=0
    while i<6:
        if isHexagonal(listJ[i]):
            listJ.pop(i)
            if 6 in done:
                done.remove(6)
        i+=1
    i=0
    while i<6:
        if isHeptagonal(listJ[i]):
            listJ.pop(i)
            if 7 in done:
                done.remove(7)
        i+=1
    i=0
    while i<6:
        if isOctagonal(listJ[i]):
            listJ.pop(i)
            if 8 in done:
                done.remove(8)
        i+=1
    if len(done)==0:
        return True
    return False

