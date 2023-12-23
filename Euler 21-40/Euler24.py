from itertools import permutations

perm=list(permutations('0123456789'))
t = [''.join(i) for i in perm]
print(t[999999])