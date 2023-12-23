def primeFact(numKO):
    answer=[]
    j=2
    numK=numKO
    while j<=numKO/2:
        firstTime=True
        while (numK/j)%1==0:
            numK/=j
            if firstTime:
                answer.append([j,1])
            else:
                answer[-1][-1]+=1
            firstTime=False
        j+=1
    return answer

num=1
while num<200000:
    if num%20000==0:
        print(num)
    if len(primeFact(num))==4 and len(primeFact(num+1))==4 and len(primeFact(num+2))==4 and len(primeFact(num+3))==4:
        print("Yes")
        if not primeFact(num)[0] in primeFact(num+1) and not primeFact(num)[0] in primeFact(num+2) and not primeFact(num)[0] in primeFact(num+3) and not primeFact(num)[1] in primeFact(num+1) and not primeFact(num)[1] in primeFact(num+2) and not primeFact(num)[1] in primeFact(num+3) and not primeFact(num)[2] in primeFact(num+1) and not primeFact(num)[2] in primeFact(num+2) and not primeFact(num)[2] in primeFact(num+3) and not primeFact(num)[3] in primeFact(num+1) and not primeFact(num)[3] in primeFact(num+2) and not primeFact(num)[3] in primeFact(num+3):
            print(num)
            break
    num+=1