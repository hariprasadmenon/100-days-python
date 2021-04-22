import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if choice == 0:
  print(rock)
elif choice == 1:
  print(paper)
elif choice == 2:
  print(scissors)
print("Computer chose:")
computer_choice = random.randint(0,2)
if computer_choice == 0:
   print(rock)
elif computer_choice == 1:
  print(paper)
else:
  print(scissors)
if choice >= 3 or choice < 0:
	print("You typed an invalid number, you lose!")
elif choice == 0 and computer_choice == 0:
  print("Draw.")
elif choice == 0 and computer_choice == 1:
  print("You loose.")
elif choice == 0 and computer_choice == 2:
  print("You win.")
elif choice == 1 and computer_choice == 0:
  print("You win.")
elif choice == 1 and computer_choice == 1:
  print("Draw.")
elif choice == 1 and computer_choice == 2:
  print("You loose.")
elif choice == 2 and computer_choice == 0:
  print("You loose.")
elif choice == 2 and computer_choice == 1:
  print("You win.")
else:
  print("Draw.")

