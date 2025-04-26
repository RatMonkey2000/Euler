eulerCoins=[1504170715041707]
eulerCoin=1504170715041707
i=0
while i<10000000:
    eulerCoin=(eulerCoin+1504170715041707)%4503599627370517
    if eulerCoin<eulerCoins[-1]:
        eulerCoins.append(eulerCoin)
    i+=1
print(sum(eulerCoins))