from itertools import permutations
handsO=open("/home/17ssoonawalla/Euler/Euler 41-60/Euler54 Poker Hands.txt", "r")
i=0
handsA=handsO.readlines()
i=0
while i<len(handsA):
    handsA[i]=handsA[i][:-1]
    i+=1

numbers=['2','3','4','5','6','7','8','9','T','J','Q','K','A']

i=0
hands=[]
while i<len(handsA):
    hands.append([handsA[i][:14],handsA[i][-14:]])
    i+=1

def royalFlush(lineStr):
    i=0
    while i<2:
        nums=[lineStr[i][0],lineStr[i][3],lineStr[i][6],lineStr[i][9],lineStr[i][12]]
        suit=lineStr[i][1]
        nums = sorted(nums, key=lambda x: numbers.index(x))
        if lineStr[i][4]==suit and lineStr[i][7]==suit and lineStr[i][10]==suit and lineStr[i][13]==suit and nums[0]=='T' and nums[1]=='J' and nums[2]=='Q' and nums[3]=='K' and nums[4]=='A':
            if i==0:
                return 'P1'
            else:
                return 'P2'
        i+=1
    return None


def straightFlush(lineStr):
    i=0
    P1=False
    P2=False
    while i<2:
        nums=[lineStr[i][0],lineStr[i][3],lineStr[i][6],lineStr[i][9],lineStr[i][12]]
        suit=lineStr[i][1]
        if lineStr[i][4]==suit and lineStr[i][7]==suit and lineStr[i][10]==suit and lineStr[i][13]==suit and nums[0] and numbers.index(nums[0])+1==numbers.index(nums[1]) and numbers.index(nums[1])+1==numbers.index(nums[2]) and numbers.index(nums[2])+1==numbers.index(nums[3]) and numbers.index(nums[3])+1==numbers.index(nums[4]) and numbers.index(nums[4])+1==numbers.index(nums[5]):
            if i==0:
                P1=True
            else:
                P2=True
        i+=1
    if not P1 and not P2:
        return None
    elif not P2:
        return 'P1'
    elif not P1:
        return 'P2'
    else:
        

def 