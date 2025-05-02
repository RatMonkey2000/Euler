eulerCoins=[1504170715041707]
eulerCoin=1504170715041707
i=0
while i<100000000000000:
    eulerCoin=(eulerCoin+1504170715041707)%4503599627370517
    if eulerCoin<eulerCoins[-1]:
        print(eulerCoin)
        eulerCoins.append(eulerCoin)
    i+=1
print(sum(eulerCoins))