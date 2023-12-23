i=143
pentList=[]
hexList=[]
triList=[]
limit=100000

for i in range(143,limit):
    pentList.append(int(i*(3*i-1)/2))
    hexList.append(int(i*(2*i-1)))
    triList.append(int(i*(i+1)/2))

#print("Yes")

def worksTrue(numI):
    if numI in pentList and numI in hexList:
        return True
    return False

num=41041
i=287
while num <hexList[-1]+1:
    print(num)
    if worksTrue(num):
        print(num)
        break
    num+=i
    i+=1