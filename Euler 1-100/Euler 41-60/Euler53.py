from math import factorial
def ifWorks(nF,rF) :
    nChooseR=factorial(nF)/(factorial(rF)*factorial(nF-rF))
    if nChooseR>1000000:
        return True
    return False

def nChosen(nS):
    counter=0
    rS=1
    while rS<nS:
        if ifWorks(nS,rS):
            counter+=1
        rS+=1
    return counter

bigCounter=0
n=1
while n<101:
    bigCounter+=nChosen(n)
    n+=1
print(bigCounter)
