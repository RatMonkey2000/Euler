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
    elif P1==True:
        return "P1"
    else:
        return "P2"

def straightFlush(lineStr):
    P1=True
    P2=True
    i=0
    while i<16:
        inputs=[lineStr[0+i],lineStr[3+i],lineStr[6+i],lineStr[9+i],lineStr[12+i]]
        inputs.sort()
        if i==0:
            inputs1=inputs
        else:
            inputs2=inputs
        if lineStr[1+i]==lineStr[4+i]==lineStr[7+i]==lineStr[10+i]==lineStr[13+i]:
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
    if not (inputs1==["2","3","4","5","6"] or inputs1==["3","4","5","6","7"] or inputs1==["4","5","6","7","8"] or inputs1==["5","6","7","8","9"] or inputs1==["6","7","8","9","T"] or inputs1==["7","8","9","T","J"] or inputs1==["8","9","T","J","Q"] or inputs1==["9","T","J","Q","K"]):
        P1=False
    if not (inputs2==["2","3","4","5","6"] or inputs2==["3","4","5","6","7"] or inputs2==["4","5","6","7","8"] or inputs2==["5","6","7","8","9"] or inputs2==["6","7","8","9","T"] or inputs2==["7","8","9","T","J"] or inputs2==["8","9","T","J","Q"] or inputs2==["9","T","J","Q","K"]):
        P2=False
    if P1==P2 and P1==False:
        return False
    elif P1==P2 and P1:
        if inputs2[-1]=="A" or (inputs2[-1]=="K" and inputs1[-1]!="A") or (inputs2[-1]=="Q" and inputs1[-1]!="A" and (inputs1[-1]!="K")) or (inputs2[-1]=="J" and inputs1[-1]!="A" and (inputs1[-1]!="K") and (inputs1[-1]!="Q")) or (inputs2[-1]=="T" and inputs1[-1]!="A" and (inputs1[-1]!="K") and (inputs1[-1]!="Q") and (inputs1[-1]!="J")) or inputs1[-1]<inputs2[-1]:
            return "P2"
        else:
            return "P1"
    elif P1==True:
        return "P1"
    else:
        return "P2"

def fourOfAKind(lineStr):
    P1=False
    P2=False
    i=0
    while i<16:
        inputs=[lineStr[0+i],lineStr[3+i],lineStr[6+i],lineStr[9+i],lineStr[12+i]]
        inputs.sort()
        print(inputs)
        if (inputs[0]==inputs[1] and inputs[0]==inputs[2] and inputs[0]==inputs[3]) or (inputs[1]==inputs[2] and inputs[1]==inputs[3] and inputs[1]==inputs[4]):
            if i==0:
                inputs1=inputs[2]
                P1=True
            else:
                if P1==True:
                    if inputs[2]>inputs1:
                        P2=True
                        P1=False
                    elif inputs[2]==inputs1:
                        return False
                else:
                    P2=True
        i+=15
    if P1:
        return "P1"
    elif P2:
        return "P2"
    else:
        return False

def fullHouse(lineStr):
    P1=False
    P2=False
    i=0
    while i<16:
        inputs=[lineStr[0+i],lineStr[3+i],lineStr[6+i],lineStr[9+i],lineStr[12+i]]
        inputs.sort()
        if (inputs[0]==inputs[1] and inputs[0]==inputs[2] and inputs[3]==inputs[4]) or (inputs[0]==inputs[1] and inputs[3]==inputs[2] and inputs[3]==inputs[4]):
            if i==0:
                P1=True
                P1M=inputs[2]
            else:
                P2=True
                P2M=inputs[2]
        i+=15
    if P1 and P2 and P1M>P2M:
        return "P1"
    elif P1 and P2 and P1M<P2M:
        return "P2"
    elif P1:
        return "P1"
    elif P2:
        return "P2"
    else:
        return False
    
def flush(lineStr):
    if lineStr[1]==lineStr[4]==lineStr[7]==lineStr[10]==lineStr[13]:
        return "P1"
    elif lineStr[16]==lineStr[19]==lineStr[22]==lineStr[25]==lineStr[28]:
        return "P2"
    else:
        return False

def straight(lineStr):
    P1==False
    P2==False
    i=0
    while i<16:
        inputs=[lineStr[0+i],lineStr[3+i],int(lineStr[6+i]),int(lineStr[9+i]),int(lineStr[12+i])]
        inputs.sort()
        if inputs==["2","3","4","5","6"] or inputs==["3","4","5","6","7"] or inputs==["4","5","6","7","8"] or inputs==["5","6","7","8","9"] or inputs==["6","7","8","9","T"] or inputs==["7","8","9","T","J"] or inputs==["8","9","T","Q","K"] or inputs==["9","T","J","Q","K"] or inputs==["T","J","Q","K","A"]:
            if i==0:
                P1=True
            else:
                P2=True
        i+=15

print(fourOfAKind("TC TC TC 3C TC QC 7C QF QG QH"))