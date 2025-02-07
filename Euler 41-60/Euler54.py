from pathlib import Path
script_dir = Path(__file__).parent
handsO= script_dir / "Euler54 Poker Hands.txt"
handsO=handsO.open("r")
i=0
handsA=handsO.readlines()
i=0
while i<len(handsA):
    handsA[i]=handsA[i][:-1]
    i+=1

i=0
hands=[]
while i<len(handsA):
    hands.append([handsA[i][:14],handsA[i][-14:]])
    i+=1

cards=['2','3','4','5','6','7','8','9','T','J','Q','K','A']


def highestCard(lineStr):
    done=False
    i=-1
    nums1=[lineStr[0][0],lineStr[0][3],lineStr[0][6],lineStr[0][9],lineStr[0][12]]
    nums1 = sorted(nums1, key=lambda x: cards.index(x))
    nums2=[lineStr[1][0],lineStr[1][3],lineStr[1][6],lineStr[1][9],lineStr[1][12]]
    nums2 = sorted(nums2, key=lambda x: cards.index(x))
    while not done:
        if cards.index(nums1[i])>cards.index(nums2[i]):
            return 'P1'
        elif cards.index(nums1[i])<cards.index(nums2[i]):
            return 'P2'
        i-=1

def royalFlush(lineStr):
    i=0
    while i<2:
        nums=[lineStr[i][0],lineStr[i][3],lineStr[i][6],lineStr[i][9],lineStr[i][12]]
        nums = sorted(nums, key=lambda x: cards.index(x))
        suit=lineStr[i][1]
        if lineStr[i][4]==suit and lineStr[i][7]==suit and lineStr[i][10]==suit and lineStr[i][13]==suit and nums[0]=='T' and nums[1]=='J' and nums[2]=='Q' and nums[3]=='K' and nums[4]=='A':
            if i==0:
                return 'P1'
            return 'P2'
        i+=1
    return None


def straightFlush(lineStr):
    i=0
    P1=False
    P2=False
    while i<2:
        nums=[lineStr[i][0],lineStr[i][3],lineStr[i][6],lineStr[i][9],lineStr[i][12]]
        nums = sorted(nums, key=lambda x: cards.index(x))
        suit=lineStr[i][1]
        if lineStr[i][4]==suit and lineStr[i][7]==suit and lineStr[i][10]==suit and lineStr[i][13]==suit and cards.index(nums[0])+1==cards.index(nums[1]) and cards.index(nums[1])+1==cards.index(nums[2]) and cards.index(nums[2])+1==cards.index(nums[3]) and cards.index(nums[3])+1==cards.index(nums[4]):
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
        nums1=[lineStr[0][0],lineStr[0][3],lineStr[0][6],lineStr[0][9],lineStr[0][12]]
        nums1=sorted(nums1, key=lambda x: cards.index(x))
        nums2=[lineStr[1][0],lineStr[1][3],lineStr[1][6],lineStr[1][9],lineStr[1][12]]
        nums2=sorted(nums2, key=lambda x: cards.index(x))
        if nums1[0]>nums2[0]:
            return 'P1'
        elif nums2[0]>nums1[0]:
            return 'P2'
        return 'TIE'
    
def fourOfAKind(lineStr):
    i=0
    P1=False
    P2=False
    while i<2:
        nums=[lineStr[i][0],lineStr[i][3],lineStr[i][6],lineStr[i][9],lineStr[i][12]]
        nums = sorted(nums, key=lambda x: cards.index(x))
        if nums[0]==nums[1] and nums[0]==nums[2] and nums[0]==nums[3] or nums[4]==nums[1] and nums[4]==nums[2] and nums[4]==nums[3]:
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
        nums1 = [lineStr[0][0],lineStr[0][3],lineStr[0][6],lineStr[0][9],lineStr[0][12]]
        nums1 = sorted(nums1, key=lambda x: cards.index(x))
        nums2 = [lineStr[1][0],lineStr[1][3],lineStr[1][6],lineStr[1][9],lineStr[1][12]]
        nums2 = sorted(nums2, key=lambda x: cards.index(x))
        if nums1[1]>nums2[1]:
            return 'P1'
        elif nums2[1]>nums1[1]:
            return 'P2'
        else:
            return highestCard(lineStr)

def fullHouse(lineStr):
    i=0
    P1=False
    P2=False
    type1=False
    while i<2:
        nums=[lineStr[i][0],lineStr[i][3],lineStr[i][6],lineStr[i][9],lineStr[i][12]]
        nums = sorted(nums, key=lambda x: cards.index(x))
        if (nums[0]==nums[1] and nums[2]==nums[1] and nums[3]==nums[4]):
            type1=True
            if i==0:
                P1=True
            else:
                P2=True
        elif (nums[4]==nums[3] and nums[2]==nums[4] and nums[0]==nums[1]):
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
        nums1 = [lineStr[0][0],lineStr[0][3],lineStr[0][6],lineStr[0][9],lineStr[0][12]]
        nums1 = sorted(nums1, key=lambda x: cards.index(x))
        nums2 = [lineStr[1][0],lineStr[1][3],lineStr[1][6],lineStr[1][9],lineStr[1][12]]
        nums2 = sorted(nums2, key=lambda x: cards.index(x))
        nums1[2]