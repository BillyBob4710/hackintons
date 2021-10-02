print("Hi if you are kool then survive. ")

print("yes")

def getDirection(description):
  userInput = input(description)
  try:
    assert isinstance(userInput, str)
    return userInput.upper()
  except:
    print("Please provide a valid input")
    getDirection(description)

def choice(health, damage):
  print("Your health is", health)
  print("Your attack damage is", damage)
  print("---------------------------------------------")

  direction = getDirection("Pick a direction R for Right L for Left.\n")

  if(direction == 'R'):
    print("After walking for a while you find a temple do you want to enter or walk around it E for Enter W for Walk around it.")
    temple = getDirection("Pick a dicesion E for Enter W for Walk")
    if(temple == 'E'):
      print("You enter the temple and right after you enter a trap triggers sending you to a tunnel leading you to an alien UFO. The End ")
    elif(temple == 'W'):
      print("You eventually Stumble upon a tribal camp and they keep you safe till the next morning then you go to a clearing and a helicopter rescues you beating the jungle!\n")
    else:
      print("You did nothing. ")
  elif(direction == 'L'):
    tiger = getDirection("You find a tiger you have two choices fight it or run R for Run F for Fight\n")
    if(tiger == 'F'): 
      print("You Fight and defeat the tiger, but you get abducted by aliens The End.")
    elif(tiger == 'R'):
      print("You run and trip on tree roots then the tiger gets abducted by aliens then you go to the extraction point and win. ")
  elif(direction == 'no'):
    print("You turn around and leave to WIN!!!!!")
  elif(direction == '/gamemode creative'):
    print("You fly away in Creative mode. ")
  
  else:
    print("You did nothing. ")


choice(100, 15)