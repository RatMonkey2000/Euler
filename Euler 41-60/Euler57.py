from fractions import Fraction

def strToList(string):
    place=string.find("/")
    List=[]
    List.append(string[:place])
    List.append(string[place+1:])
    return(List)

def isTopHeavy(numK):
    print(numK)
    frac=Fraction(numK)
    frac=str(frac)
    frac=strToList(frac)
    print(frac)
    if len(str(frac[0]))>len(str(frac[1])):
        print(frac)
        return True
    return False

def iter(numJ):
    totNum=0
    i=0
    while i<200:
        numJ+=1
        numJ=1+1/numJ
        if isTopHeavy(numJ):
            totNum+=1
        i+=1
    return(totNum)

print(iter(1))