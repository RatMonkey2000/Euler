from math import sqrt
import ast
def wordValue(word):
    alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    score=0
    n=0
    while n<len(word):
        score+=alphabet.index(word[n])+1
        n+=1
    return(score)

def triTrue(num):
    a=num*2
    i=1
    while i<sqrt(a)+1:
        if i**2+i==a:
            return True
        i+=1
    return False
words=(open("/Users/samsoonawalla/Downloads/Words.txt","r"))
words=words.read()
words = ast.literal_eval(words)
j=0
numTri=0
while j<len(words):
    if triTrue(wordValue(words[j])):
        numTri+=1
    j+=1
print(numTri)
