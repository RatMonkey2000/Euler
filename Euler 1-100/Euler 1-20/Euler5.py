i=2
num=20
while num<9999999999999:
    while i<21:
        if num%i*2==0:
            i+=1
        else:
            works=False
            break
    if works==True:
        print(num)
        exit()
    num+=1
    i=2
    works=True
