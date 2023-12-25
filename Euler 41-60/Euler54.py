from linecache import getline
from itertools import permutations
file=open("C:/Users/kazbi/Downloads/Euler54 Poker Hands.txt", "r")
i=0
def royalFlush(lineStr):
    P1=False
    P2=False
    i=0
    while i<16:
        inputs=[lineStr[0+i],lineStr[3+i],lineStr[6+i],lineStr[9+i],lineStr[12+i]]
        perm=list(permutations(inputs))
        if ('T','J','Q','K','A') in perm and lineStr[1+i]==lineStr[4+i]==lineStr[7+i]==lineStr[10+i]==lineStr[13+i]and i==0:
            P1=True
        if ('T','J','Q','K','A') in perm and lineStr[1+i]==lineStr[4+i]==lineStr[7+i]==lineStr[10+i]==lineStr[13+i]and i==15:
            P2=True
        i+=15
    if P1==P2 and P1==False:
        return False
    elif P1==P2 and P2:
        return True
    elif P1==True:
        return "P1"
    elif i==15:
        return "P2"

def straightFlush(lineStr):
    P1=True
    P2=True
    i=0
    while i<16:
        if lineStr[1+i]==lineStr[4+i]==lineStr[7+i]==lineStr[10+i]==lineStr[13+i]:
            inputs=[lineStr[0+i],lineStr[3+i],lineStr[6+i],lineStr[9+i],lineStr[12+i]]
            inputs.sort()
            if i==0:
                inputs1=inputs
            else:
                inputs2=inputs
            j=1
            while j<5:
                if (inputs[j]=="T" and inputs[j-1]=="9") or (inputs[j]=="J" and inputs[j-1]=="T") or (inputs[j]=="Q" and inputs[j-1]=="J") or (inputs[j]=="K" and inputs[j-1]=="Q") or (inputs[j]=="A" and inputs[j-1]=="K") and int(inputs[j])!=int(inputs[j-1])+1:
                    if i==0:
                        P1=False
                    else:
                        P2=False
                j+=1
        else:
            if i==0:
                P1=False
            else:
                P2=False
        i+=15
    if P1==P2 and P1==False:
        return False
    elif P1==P2 and P1:
        if inputs1[-1]<inputs2[-1]:
            return "P2"
        else:
            return "P1"
    elif P1==True:
        return "P1"
    else:
        return "P2"

def fourOfAKind(lineStr):
    P1=True
    P2=True
    i=0
    while i<16:
        i+=1