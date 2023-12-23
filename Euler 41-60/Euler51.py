from itertools import permutations
import ast
primes=open(r"C:\users\kazbi\Downloads\Primes.txt","r")
primes=ast.literal_eval(primes.read())

def prime(numK):
    if numK in primes:
        return True
    return False

def replacePos(numJ,j):
    numCounter=0
    numJ=str(numJ)
    #j=str(j)
    i=0
    while i<10:
        k=0
        numJChange=numJ
        while k<len(j):
            numJChange = numJChange[:int(j[k])] + str(i) + numJChange[int(j[k])+1:]
            k+=1
        if prime(int(numJChange)):
            numCounter+=1
        i+=1
    if numCounter==8:
        return True
    return False

def allReplacePos(numP):
    p=1
    permOptions=[]
    while p<len(str(numP))+1:
        permOptions.append(p)
        p+=1
    p=1
    while p<len(str(numP))+1:
        perm=list(permutations(permOptions,p))
        perm=[list(ele) for ele in perm]
        m=0
        while m<len(perm):
            if replacePos(numP,perm[m]):
                return True
            m+=1
        p+=1
    return False


num=60000
while num<len(primes):
    print(num)
    if allReplacePos(num):
        print(num)
        break
    num+=1