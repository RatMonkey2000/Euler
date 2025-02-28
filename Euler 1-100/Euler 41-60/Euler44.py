penList = []
limit=5001
lowestD=10000000000000000000000

for i in range(1,limit):
    penList.append(int(i * (3 * i - 1) / 2))

print(penList)

def penTrue(num):
    if num in penList:
        return True
    return False

def works(a,b):
    if penTrue(a + b) and penTrue(a-b):
        print(a)
        print(b)
        if 0-b+a<lowestD:
            lowestD=0-b+a

i=0
while i < len(penList):
    l = i + 1
    while l < len(penList):
        j = penList[i]
        k = penList[l]
        works(k,j)
        l += 1
    i += 1
print(lowestD)
