from math import sqrt
import threading

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
    


def check1():
    num=3
    Sum=0
    while num<101:
        if isnatural(num**2):
            Sum+=num**2
        num+=8

def check1():
    num=4
    Sum=0
    while num<101:
        if isnatural(num**2):
            Sum+=num**2
        num+=8
def check1():
    num=5
    Sum=0
    while num<101:
        if isnatural(num**2):
            Sum+=num**2
        num+=8

def check1():
    num=6
    Sum=0
    while num<101:
        if isnatural(num**2):
            Sum+=num**2
        num+=8

def check1():
    num=7
    Sum=0
    while num<101:
        if isnatural(num**2):
            Sum+=num**2
        num+=8

def check1():
    num=8
    Sum=0
    while num<101:
        if isnatural(num**2):
            Sum+=num**2
        num+=8

def check1():
    num=9
    Sum=0
    while num<101:
        if isnatural(num**2):
            Sum+=num**2
        num+=8
def check1():
    num=10
    Sum=0
    while num<101:
        if isnatural(num**2):
            Sum+=num**2
        num+=8

t1=threading.Thread(check1,)