coins=[1,2,5,10,20,50,100,200]
def ways(coins,n,Sum):
	if Sum<0:
		return 0
	if Sum==0:
		return 1
	if n<=0:
		return 0
	return ways(coins,n-1,Sum)+ways(coins,n,Sum-coins[n-1])
print(ways(coins,8,200))