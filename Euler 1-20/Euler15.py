# You must make 40 moves in any order
# At the beggining there are two choises you can make etc.

box=[[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]]

i=1
j=1
box
while i<21:
    j=i
    while j<21:
        box[i].append(box[i-1][j]+box[i][j-1])
        if i!=j:
            box[j].append(box[i][j])
        j+=1
    i+=1
print(box[i-1][j-1])
