n=1
def factor(num):
    j=2
    factors=[1]
    while j<num+1:
        if num%j==0:
            factors.append(num)
        j+=1
    return len(factors)


i=2
while factor(n)<501:
    n+=i
    i+=1
print(n)

