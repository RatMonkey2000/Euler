from random import randint
cards=['2','3','4','5','6','7','8','9','T','J','Q','K','A']

def highestCard(lineStr):
    done=False
    i=-1
    nums1=[lineStr[0][0],lineStr[0][3],lineStr[0][6],lineStr[0][9],lineStr[0][12]]
    nums1 = sorted(nums1, key=lambda x: cards.index(x))
    nums2=[lineStr[1][0],lineStr[1][3],lineStr[1][6],lineStr[1][9],lineStr[1][12]]
    nums2 = sorted(nums2, key=lambda x: cards.index(x))
    while not done and i>-6:
        if cards.index(nums1[i])>cards.index(nums2[i]):
            return 'P1'
        elif cards.index(nums1[i])<cards.index(nums2[i]):
            return 'P2'
        i-=1
    return 'TIE'

def royalFlush(lineStr):
    i=0
    P1=False
    P2=False
    while i<2:
        nums=[lineStr[i][0],lineStr[i][3],lineStr[i][6],lineStr[i][9],lineStr[i][12]]
        nums = sorted(nums, key=lambda x: cards.index(x))
        suit=lineStr[i][1]
        if lineStr[i][4]==suit and lineStr[i][7]==suit and lineStr[i][10]==suit and lineStr[i][13]==suit and nums[0]=='T' and nums[1]=='J' and nums[2]=='Q' and nums[3]=='K' and nums[4]=='A':
            if i==0:
                P1=True
            else:
                P2=True
        i+=1
    if not P1 and not P2:
        return None
    elif not P1:
        return 'P2'
    elif not P2:
        return 'P1'
    return 'TIE'


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
        if cards.index(nums1)[0]>cards.index(nums2[0]):
            return 'P1'
        elif cards.index(nums1)[0]<cards.index(nums2[0]):
            return 'P2'
        return 'TIE'
    
def fourOfAKind(lineStr):
    i=0
    P1=False
    P2=False
    while i<2:
        nums=[lineStr[i][0],lineStr[i][3],lineStr[i][6],lineStr[i][9],lineStr[i][12]]
        nums = sorted(nums, key=lambda x: cards.index(x))
        if (nums[0]==nums[1] and nums[0]==nums[2] and nums[0]==nums[3]) or (nums[4]==nums[1] and nums[4]==nums[2] and nums[4]==nums[3]):
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
        if cards.index(nums1[1])>cards.index(nums2[1]):
            return 'P1'
        elif cards.index(nums1[1])<cards.index(nums2[1]):
            return 'P2'
        else:
            return highestCard(lineStr)

def fullHouse(lineStr):
    i=0
    P1=False
    P2=False
    type1=False
    type2=False
    while i<2:
        nums=[lineStr[i][0],lineStr[i][3],lineStr[i][6],lineStr[i][9],lineStr[i][12]]
        nums = sorted(nums, key=lambda x: cards.index(x))
        if (nums[0]==nums[1] and nums[2]==nums[1] and nums[3]==nums[4]):
            if i==0:
                P1=True
                type1=True
            else:
                P2=True
                type2=True
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
        if cards.index(nums1[2])>cards.index(nums2[2]):
            return 'P1'
        elif cards.index(nums1[2])<cards.index(nums2[2]):
            return 'P2'
        elif type1 and type2 and cards.index(nums1[4])>cards.index(nums2[4]):
            return 'P1'
        elif type1 and type2 and cards.index(nums1[4])<cards.index(nums2[4]):
            return 'P2'
        elif type1 and not type2 and cards.index(nums1[4])<cards.index(nums2[0]):
            return 'P2'
        elif type1 and not type2 and cards.index(nums1[4])>cards.index(nums2[0]):
            return 'P1'
        elif not type1 and type2 and cards.index(nums1[0])>cards.index(nums2[4]):
            return 'P1'
        elif not type1 and type2 and cards.index(nums1[0])<cards.index(nums2[4]):
            return 'P2'
        elif not type1 and not type2 and cards.index(nums1[0])<cards.index(nums2[0]):
            return 'P2'
        elif not type1 and not type2 and cards.index(nums1[0])>cards.index(nums2[0]):
            return 'P1'
        return highestCard(lineStr)

def flush(lineStr):
    i=0
    P1=False
    P2=False
    i=0
    while i<2:
        suit=lineStr[i][1]
        if lineStr[i][4]==suit and lineStr[i][7]==suit and lineStr[i][10]==suit and lineStr[i][13]==suit:
            if i==0:
                P1=True
            else:
                P2=True
        i+=1
    if not P1 and not P2:
        return None
    elif not P1:
        return 'P2'
    elif not P2:
        return 'P1'
    return highestCard(lineStr)

def straight(lineStr):
    i=0
    P1=False
    P2=False
    while i<2:
        nums=[lineStr[i][0],lineStr[i][3],lineStr[i][6],lineStr[i][9],lineStr[i][12]]
        nums = sorted(nums, key=lambda x: cards.index(x))
        if cards.index(nums[0])+1==cards.index(nums[1]) and cards.index(nums[1])+1==cards.index(nums[2]) and cards.index(nums[2])+1==cards.index(nums[3]) and cards.index(nums[3])+1==cards.index(nums[4]):
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
        if cards.index(nums1[0])>cards.index(nums2[0]):
            return 'P1'
        elif cards.index(nums2[0])>cards.index(nums1[0]):
            return 'P2'
        return 'TIE'

def threeOfAKind(lineStr):
    i=0
    P1=False
    P2=False
    while i<2:
        nums=[lineStr[i][0],lineStr[i][3],lineStr[i][6],lineStr[i][9],lineStr[i][12]]
        nums = sorted(nums, key=lambda x: cards.index(x))
        if (nums[0]==nums[1] and nums[0]==nums[2]) or (nums[1]==nums[2] and nums[1]==nums[3]) or (nums[2]==nums[3] and nums[2]==nums[4]):
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
        if cards.index(nums1[2])>cards.index(nums2[2]):
            return 'P1'
        elif cards.index(nums2[2])>cards.index(nums1[2]):
            return 'P2'
        return highestCard(lineStr)
    
def twoPairs(lineStr):
    i=0
    P1=False
    P2=False
    while i<2:
        nums=[lineStr[i][0],lineStr[i][3],lineStr[i][6],lineStr[i][9],lineStr[i][12]]
        nums=sorted(nums, key=lambda x: cards.index(x))
        if (nums[0]==nums[1] and nums[2]==nums[3]):
            if i==0:
                P1=True
            else:
                P2=True
        if (nums[0]==nums[1] and nums[3]==nums[4]) or (nums[1]==nums[2] and nums[3]==nums[4]):
            if i==0:
                P1=True
            else:
                P2=True
        i+=1
    if not P1 and not P2:
        return None
    elif not P1:
        return 'P2'
    elif not P2:
        return 'P1'
    else:
        nums1=[lineStr[0][0],lineStr[0][3],lineStr[0][6],lineStr[0][9],lineStr[0][12]]
        nums1=sorted(nums1, key=lambda x: cards.index(x))
        nums2=[lineStr[1][0],lineStr[1][3],lineStr[1][6],lineStr[1][9],lineStr[1][12]]
        nums2=sorted(nums2, key=lambda x: cards.index(x))
        if cards.index(nums1[3])>cards.index(nums2[3]):
            return 'P1'
        elif cards.index(nums1[3])<cards.index(nums2[3]):
            return 'P2'
        else:
            if cards.index(nums1[1])>cards.index(nums2[1]):
                return 'P1'
            elif cards.index(nums1[1])<cards.index(nums2[1]):
                return 'P2'
            return highestCard(lineStr)
        
def onePair(lineStr):
    i=0
    P1=False
    P2=False
    place1=0
    place2=0
    while i<2:
        nums=[lineStr[i][0],lineStr[i][3],lineStr[i][6],lineStr[i][9],lineStr[i][12]]
        nums=sorted(nums, key=lambda x: cards.index(x))
        if nums[0]==nums[1]:
            if i==0:
                P1=True
                place1=0
            else:
                P2=True
                place2=0
        if nums[1]==nums[2]:
            place=1
            if i==0:
                P1=True
                place1=1
            else:
                P2=True
                place2=1
        if nums[2]==nums[3]:
            place=2
            if i==0:
                P1=True
                place1=2
            else:
                P2=True
                place2=2
        if nums[3]==nums[4]:
            place=3
            if i==0:
                P1=True
                place1=3
            else:
                P2=True
                place2=3
        i+=1
    if not P1 and not P2:
        return None
    elif not P1:
        return 'P2'
    elif not P2:
        return 'P1'
    else:
        nums1=[lineStr[0][0],lineStr[0][3],lineStr[0][6],lineStr[0][9],lineStr[0][12]]
        nums1=sorted(nums1, key=lambda x: cards.index(x))
        nums2=[lineStr[1][0],lineStr[1][3],lineStr[1][6],lineStr[1][9],lineStr[1][12]]
        nums2=sorted(nums2, key=lambda x: cards.index(x))
        if cards.index(nums1[place1])>cards.index(nums2[place2]):
            return 'P1'
        elif cards.index(nums1[place1])<cards.index(nums2[place2]):
            return 'P2'
        else:
            return highestCard(lineStr)


def checkWinner(lineStr):
    if royalFlush(lineStr)=='P1':
        return True
    elif royalFlush(lineStr)=='P2' or royalFlush(lineStr)=='TIE':
        return False
    elif straightFlush(lineStr)=='P1':
        return True
    elif straightFlush(lineStr)=='P2' or straightFlush(lineStr)=='TIE':
        return False
    elif fourOfAKind(lineStr)=='P1':
        return True
    elif fourOfAKind(lineStr)=='P2' or fourOfAKind(lineStr)=='TIE':
        return False
    elif fullHouse(lineStr)=='P1':
        return True
    elif fullHouse(lineStr)=='P2' or fullHouse(lineStr)=='TIE':
        return False
    elif flush(lineStr)=='P1':
        return True
    elif flush(lineStr)=='P2' or flush(lineStr)=='TIE':
        return False
    elif straight(lineStr)=='P1':
        return True
    elif straight(lineStr)=='P2'  or straight(lineStr)=='TIE':
        return False
    elif threeOfAKind(lineStr)=='P1':
        return True
    elif threeOfAKind(lineStr)=='P2' or threeOfAKind(lineStr)=='TIE':
        return False
    elif twoPairs(lineStr)=='P1':
        return True
    elif twoPairs(lineStr)=='P2' or twoPairs(lineStr)=='TIE':
        return False
    elif onePair(lineStr)=='P1':
        return True
    elif onePair(lineStr)=='P2' or onePair(lineStr)=='TIE':
        return False
    elif highestCard(lineStr)=='P1':
        return True
    return False

balence=1000
suits=['S','H','D','C']
while True:
    print("Balence ",balence)
    hand1=f"{cards[randint(0,12)]}{suits[randint(0,3)]} {cards[randint(0,12)]}{suits[randint(0,3)]} {cards[randint(0,12)]}{suits[randint(0,3)]} {cards[randint(0,12)]}{suits[randint(0,3)]} {cards[randint(0,12)]}{suits[randint(0,3)]}"
    print(hand1)
    hand2=f"{cards[randint(0,12)]}{suits[randint(0,3)]} {cards[randint(0,12)]}{suits[randint(0,3)]} {cards[randint(0,12)]}{suits[randint(0,3)]} {cards[randint(0,12)]}{suits[randint(0,3)]} {cards[randint(0,12)]}{suits[randint(0,3)]}"
    bet=input("Place Bet or FOLD   ")
    if bet=="FOLD":
        balence-=bet
        continue
    bet=int(bet)
    if bet>balence:
        print("TOO HIGH")
        continue
    if not checkWinner([hand1,hand2]):
        print(f"You have been raised to {bet+randint(1,100)}")
        raises=input("Fold or Raise   ")
        if raises=="FOLD":
            balence-=bet
            continue
        raises=int(raises)
        bet+=raises
        print(bet)
        if bet>balence:
            print("TOO HIGH")
            continue
        else:
            print(f"You have been raised to {bet+randint(0,100)}")
            raises=input("Fold or Raise   ")
            if raises=="FOLD":
                balence-=bet
                continue
            raises=int(raises)
            bet+=raises
            if bet>balence:
                print("TOO HIGH")
                continue
    else:
        print("FOLD!")