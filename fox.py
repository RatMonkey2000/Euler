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
    print(" Fox")
  if chicken==0:
    print(" Chicken")
  if grain==0:
    print(" Grain")
  if farmer==0:
    print(" You")
  print("On Right Side")
  if fox==1:
    print(" Fox")
  if chicken==1:
    print(" Chicken")
  if grain==1:
    print(" Grain")
  if farmer==1:
    print(" You")
    
def isCorrect():
  if fox==1 and chicken==1 and grain==1 and farmer==1:
    return True
  return False
  

print("""
A fox, chicken and a bag of grain wait by the side of a river.
Which item will you take in your rowboat to the other side?
Fox, Chicken, Grain or None?""")
choise=input("Choose: ")
fox=0
chicken=0
grain=0
farmer=0
if choise=="None" or choise=="none" or choise=="NONE":
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
    chicken=(chicken+1)%2
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
while not isCorrect():
  isWrong()
  state()
  print("Fox, Chicken, Grain, or None?")
  choise=input("Choose: ")
  if choise=="None" or choise=="none" or choise=="NONE":
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
      chicken=(chicken+1)%2
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
  
print("You Win!!!")