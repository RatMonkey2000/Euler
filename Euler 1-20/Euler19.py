dayN=1
day=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
month=["january","february","march","april","may","june","july","august","september","october","november","december"]
year=1900
i=0
j=0
while i<12:
 dayN=1
 if i==0 or i==2 or i==4 or i==6 or i==7 or i==9 or i==11:
  while dayN<32:
   dayN+=1
   if j!=6:
    j+=1
   else:
    j=0
 elif i==3 or i==5 or i==8 or i==10:
  while dayN<31:
   dayN+=1
   if j!=6:
    j+=1
   else:
    j=0
 else:
  if year%100!=0:
   if year%4==0:
    while dayN<30:
     dayN+=1
     if j!=6:
      j+=1
     else:
      j=0
   else:
    while dayN<29:
     dayN+=1
     if j!=6:
      j+=1
     else:
      j=0
  else:
   if year%400==0:
    while dayN<30:
     dayN+=1
     if j!=6:
      j+=1
     else:
      j=0
   else:
    while dayN<29:
     dayN+=1
     if j!=6:
      j+=1
     else:
      j=0
 i+=1
year=1901
count=0
while year<2001:
 i=0
 while i<12:
  dayN=1
  if i==0 or i==2 or i==4 or i==6 or i==7 or i==9 or i==11:
   while dayN<32:
    if j!=6:
     j+=1
    else:
     if dayN==1:
      count+=1
     j=0
    dayN+=1
  elif i==3 or i==5 or i==8 or i==10:
   while dayN<31:
    if j!=6:
     j+=1
    else:
     if dayN==1:
      count+=1
     j=0
    dayN+=1
  else:
   if year%100!=0:
    if year%4==0:
     while dayN<30:
      if j!=6:
       j+=1
      else:
       if dayN==1:
        count+=1
       j=0
      dayN+=1
    else:
     while dayN<29:
      if j!=6:
       j+=1
      else:
       if dayN==1:
        count+=1
       j=0
      dayN+=1
   else:
    if year%400==0:
     while dayN<30:
      if j!=6:
       j+=1
      else:
       if dayN==1:
        count+=1
       j=0
      dayN+=1
    else:
     while dayN<29:
      if j!=6:
       j+=1
      else:
       if dayN==1:
        count+=1
       j=0
      dayN+=1
  i+=1
 year+=1
print(count)
