num1=999
num2=999
highest=0
works=True
while num1>99:
    num2=999
    while num2>99:
        palindrome=num1*num2
        works=True
        i=0
        if len(str(palindrome))%2==0:
            while i<len(str(palindrome))/2:
                if str(palindrome)[i]==str(palindrome)[-i-1]:
                    i+=1
                else:
                    works=False
                    break
            if works==True:
                if highest<palindrome:
                    highest=palindrome
        else:
            while i<len(str(palindrome))/2-0.5:
                if str(palindrome)[i]==str(palindrome)[-i-1]:
                    i+=1
                else:
                    works=False
                    break
            if works==True:
                if highest<palindrome:
                    highest=palindrome
        num2-=1
    num1-=1
print(highest)
