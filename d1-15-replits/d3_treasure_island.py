print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
path = input("You are stranded on an island. Choose your path. Will you turn 'Left' or 'Right'? \n").lower()
if path != "left":
  print("You have fallen into a bottomless pit. This is the end of your journey. Game Over")
elif path =="left":
  lake = input("You are at the edge of a vast sprawling lake.Do you go for a 'Swim' or 'Wait'? \n").lower()
  if lake != "wait":
    print("Oh no! A trout has swallowed you whole. It's the end of the line for you. Game Over")
  elif lake == "wait":
    door = input("Three doors have appeared. Which one do you enter, 'Red', 'Yellow' or 'Blue'? \n").lower()
    if door == "red":
      print("The heat, its too much to bear. Alas you have been reduced to nothing but char. Game Over")
    elif door == "blue":
      print("Blue was never your color. Hungry beasts have eaten you alive. A sad end! Game Over")
    elif door == "yellow":
      print('''Oh my! What a wonderful sight. A large pile of gold all for your taking. This has been a fruitful juorney. You win!''')
    else:
      print("Error 404! Game over.")


