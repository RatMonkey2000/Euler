message=input()
i=0
frequency=[]
chars=[]
while i<len(message):
    if not message[i] in chars:
        chars.append(message[i])
        frequency.append(0)
    frequency[chars.index(message[i])]+=1
    i+=1

chars=sorted(chars, key=lambda x: 0-frequency[chars.index(x)])
frequency=sorted(frequency, reverse=True)
print(chars)
print(frequency)