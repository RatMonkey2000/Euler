from itertools import permutations
def multDig(numK):
    k=1
    perms = permutations(str(numK))
    permuted_lists = [''.join(map(str, perm)) for perm in perms]
    while k<7:
        if not str(k*numK) in permuted_lists:
            return False
        k+=1
    return True


num=1
while num<1000000000000:
    if multDig(num):
        print(num)
        break
    num+=1