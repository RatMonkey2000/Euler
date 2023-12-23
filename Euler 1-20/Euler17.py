num=0
sumNum=0
length=len(str(num))
for num in range(0,1001):
    length=len(str(num))
    if int(str(num)[length-1])==1:
        sumNum+=3
    if int(str(num)[length-1])==2:
        sumNum+=3
    if int(str(num)[length-1])==3:
         sumNum+=5
    if int(str(num)[length-1])==4:
        sumNum+=4
    if int(str(num)[length-1])==5:
        sumNum+=4
    if int(str(num)[length-1])==6:
        sumNum+=3
    if int(str(num)[length-1])==7:
        sumNum+=5
    if int(str(num)[length-1])==8:
        sumNum+=5
    if int(str(num)[length-1])==9:
        sumNum+=4
    if length>1:
        if int(str(num)[length-2])==1:
            if int(str(num)[length-1])==0:
                sumNum+=3
            if int(str(num)[length-1])==1:
                sumNum-=3
                sumNum+=6
            if int(str(num)[length-1])==2:
                sumNum-=3
                sumNum+=6
            if int(str(num)[length-1])==3:
                sumNum-=5
                sumNum+=8
            if int(str(num)[length-1])==4:
                sumNum-=4
                sumNum+=8
            if int(str(num)[length-1])==5:
                sumNum-=4
                sumNum+=7
            if int(str(num)[length-1])==6:
                sumNum-=3
                sumNum+=7
            if int(str(num)[length-1])==7:
                sumNum-=5
                sumNum+=9
            if int(str(num)[length-1])==8:
                sumNum-=5
                sumNum+=8
            if int(str(num)[length-1])==9:
                sumNum-=4
                sumNum+=8
        if int(str(num)[length-2])==2:
            sumNum+=6
        if int(str(num)[length-2])==3:
            sumNum+=6
        if int(str(num)[length-2])==4:
            sumNum+=6
        if int(str(num)[length-2])==5:
            sumNum+=5
        if int(str(num)[length-2])==6:
            sumNum+=5
        if int(str(num)[length-2])==7:
            sumNum+=7
        if int(str(num)[length-2])==8:
            sumNum+=6
        if int(str(num)[length-2])==9:
            sumNum+=5
    if length==3:
        sumNum+=7
        if int(str(num)[length-1])!=0 or int(str(num)[length-2])!=0:
            sumNum+=3
        if int(str(num)[length-3])==1:
            sumNum+=3
        if int(str(num)[length-3])==2:
            sumNum+=3
        if int(str(num)[length-3])==3:
            sumNum+=5
        if int(str(num)[length-3])==4:
            sumNum+=4
        if int(str(num)[length-3])==5:
            sumNum+=4
        if int(str(num)[length-3])==6:
            sumNum+=3
        if int(str(num)[length-3])==7:
            sumNum+=5
        if int(str(num)[length-3])==8:
            sumNum+=5
        if int(str(num)[length-3])==9:
            sumNum+=4
    if length==4:
        sumNum+=11
print(sumNum)
