num=1
sumOfSquares=0
squareOfSum=0
while num<101:
    sumOfSquares+=(num**2)
    squareOfSum+=num
    num+=1
print(squareOfSum**2-sumOfSquares)
