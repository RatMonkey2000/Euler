def isWrong():
  if fox==chicken and chicken!=farmer:
    print("Fox eats chicken. You Lose!!!")
    exit()
  elif grain==chicken and chicken!=farmer:
    print("Chicken eats grain. You Lose!!!")
    exit()

def state():
  print("On Wrong side of River:")
  if fox==0:
    print("fox")
  if chicken==0:
    print("chicken")
  if grain==0:
    print("grain")
  if farmer==0:
    print("farmer")
  print("On Right Side")
  if fox==1:
    print("fox")
  if chicken==1:
    print("chicken")
  if grain==1:
    print("grain")
  if farmer==1:
    print("farmer")
    
def isCorrect():
  if fox==1 and chicken==1 and grain==1 and farmer==1:
    return True
  return False
  

print("""
A fox, chicken and a bag of grain wait by the side of a river.
Which item will you take in your rowboat to the other side?
fox, chicken, grain or farmer?""")
choise=input("Choose:")
fox=0
chicken=0
grain=0
farmer=0
if choise=="Farmer" or choise=="farmer" or choise=="FARMER":
  farmer=(farmer+1)%2
elif choise=="Fox" or choise=="fox" or choise=="FOX":
  if fox==farmer:
    farmer=(farmer+1)%2
    fox=(fox+1)%2
  else:
    print("Invalid! Start again!")
    exit()
elif choise=="Chicken" or choise=="chicken" or choise=="CHICKEN":
  if chicken==farmer:
    farmer=(farmer+1)%2
    chicken=(chicken)%2
  else:
    print("Invalid! Start again!")
    exit()
elif choise=="Grain" or choise=="grain" or choise=="GRAIN":
  if grain==farmer:
    farmer=(farmer+1)%2
    grain=(grain+1)%2
  else:
    print("Invalid! Start again!")
    exit()
else:
  print("Invalid! Start again!")
  exit()
while not isCorrect:
  state()
  choise=input("Choose:")
  if choise=="Farmer" or choise=="farmer" or choise=="FARMER":
    farmer=(farmer+1)%2
  elif choise=="Fox" or choise=="fox" or choise=="FOX":
    if fox==farmer:
      farmer=(farmer+1)%2
      fox=(fox+1)%2
    else:
      print("Invalid! Start again!")
      exit()
  elif choise=="Chicken" or choise=="chicken" or choise=="CHICKEN":
    if chicken==farmer:
      farmer=(farmer+1)%2
      chicken=(chicken)%2
    else:
      print("Invalid! Start again!")
      exit()
  elif choise=="Grain" or choise=="grain" or choise=="GRAIN":
    if grain==farmer:
      farmer=(farmer+1)%2
      grain=(grain+1)%2
    else:
      print("Invalid! Start again!")
      exit()
  iswrong()
  
print("You Win!!!)