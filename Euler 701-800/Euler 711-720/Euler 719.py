from math import sqrt
import multiprocessing

def listWorks(listi):
    i=0
    sumNum=0
    while i<len(listi):
        if listi[i]!=None and listi[i]!='00' and listi[i]!='000' and listi[i]!='0000' and listi[i]!='00000' and listi[i]!='000000':
            sumNum+=int(listi[i])
        i+=1
    return sumNum

def nextPerm(listi):
    i=0
    while i<len(listi):
        if len(listi[i])!=1:
            if listi[i+1]==None:
                listi[i+1]=listi[i][-1]
                listi[i]=listi[i][:-1]
            else:
                listi[i+1]=listi[i][-1]+listi[i+1]
                listi[i]=listi[i][:-1]
            return listi
        else:
            i+=1
    return False

def isnatural(num):
    i=1
    splits=[]
    splits.append(str(num))
    while i<len(str(num)):
        splits.append(None)
        i+=1
    done=False
    while not done:
        if listWorks(splits)==sqrt(num):
            done=True
            break
        splits=nextPerm(splits)
        if splits==False:
            break
    if done:
        return True
    return False
    


total=0
Sum1=0
Sum2=0
Sum3=0
Sum4=0
Sum5=0
Sum6=0
Sum7=0
Sum8=0
def check1():
    global total
    num=3
    global Sum1
    while num<1000001:
        if isnatural(num**2):
            Sum1+=num**2
        num+=8
def check2():
    global total
    num=4
    global Sum2
    while num<1000001:
        if isnatural(num**2):
            Sum2+=num**2
        num+=8
def check3():
    global total
    num=5
    Sum3=0
    while num<1000001:
        if isnatural(num**2):
            Sum3+=num**2
        num+=8
def check4():
    global total
    num=6
    Sum4=0
    while num<1000001:
        if isnatural(num**2):
            Sum4+=num**2
        num+=8
def check5():
    global total
    num=7
    Sum5=0
    while num<1000001:
        if isnatural(num**2):
            Sum5+=num**2
        num+=8
def check6():
    global total
    num=8
    Sum6=0
    while num<1000001:
        if isnatural(num**2):
            Sum6+=num**2
        num+=8
def check7():
    global total
    num=9
    Sum7=0
    while num<1000001:
        if isnatural(num**2):
            Sum7+=num**2
        num+=8
def check8():
    global total
    num=10
    Sum8=0
    while num<1000001:
        if isnatural(num**2):
            Sum8+=num**2
        num+=8
    print(Sum8)
    

t1=multiprocessing.Process(target=check1)
t2=multiprocessing.Process(target=check2)
t3=multiprocessing.Process(target=check3)
t4=multiprocessing.Process(target=check4)
t5=multiprocessing.Process(target=check5)
t6=multiprocessing.Process(target=check6)
t7=multiprocessing.Process(target=check7)
t8=multiprocessing.Process(target=check8)
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
print(Sum1+Sum2+Sum3+Sum4+Sum5+Sum6+Sum7+Sum8)