from fractions import Fraction
def isTopHeavy(numK):
    frac=Fraction(numK)
    print(frac)
    if len(str(frac))>len(str(frac)):
        return True
    return False

def iter(numJ):
    totNum=0
    i=0
    while i<10:
        numJ+=1
        numJ=1+1/numJ
        print(numJ)
        if isTopHeavy(numJ):
            totNum+=1
        i+=1
    return(totNum)

print(iter(1))