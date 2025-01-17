from itertools import permutations
hands=open("/home/17ssoonawalla/Euler/Euler 41-60/Euler54 Poker Hands.txt", "r")
i=0
hands=hands.readlines()
i=0
while i<len(hands):
    hands[i]=hands[i][:-1]
    i+=1

def makeList(hand):
    print(hands)

makeList("asdf")
def royalFlush(lineStr):
    P1=False
    P2=False