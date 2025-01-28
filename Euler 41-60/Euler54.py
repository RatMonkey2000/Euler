from itertools import permutations
handsO=open("/home/17ssoonawalla/Euler/Euler 41-60/Euler54 Poker Hands.txt", "r")
i=0
handsA=handsO.readlines()
i=0
while i<len(handsA):
    handsA[i]=handsA[i][:-1]
    i+=1

numbers=[2,3,4,5,6,7,8,9,'T','J','Q','K','A']

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
        if lineStr[i][4]==suit and lineStr[i][7]==suit and lineStr[i][10]==suit and lineStr[i][13]==suit and 'A' in nums and 'K' in nums and 'Q' in nums and 'J' in nums and 'T' in nums:
            if i==0:
                return 'P1'
            else:
                return 'P2'
        i+=1
    return None

def straightFlush(lineStr):
    i=0
    while i<2:
        nums=[lineStr[i][0],lineStr[i][3],lineStr[i][6],lineStr[i][9],lineStr[i][12]]
        suit=lineStr[i][1]
        if lineStr[i][4]==suit and lineStr[i][7]==suit and lineStr[i][10]==suit and lineStr[i][13]==suit and nums[1]