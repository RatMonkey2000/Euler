from itertools import permutations
num='0123456789'
numList=list(map("".join, permutations(num)))
i=0
Sum=0
ideal=['does not matter',2,3,5,7,11,13,17]
while i<len(numList):
    works=True
    n=numList[i]
    j=1
    while j<8 and works:
        if not float(str(n)[j]+str(n)[j+1]+str(n)[j+2])%ideal[j]==0:
            works=False
        j+=1
    if works:
        Sum+=int(n)
    i+=1
print(Sum)
