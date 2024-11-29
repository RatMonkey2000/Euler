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
    numJ=2/6+sqrt(n/3+)