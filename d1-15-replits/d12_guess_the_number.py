#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from replit import clear
from art import logo
  
def play_game(level):
  if level == "easy":
    attempts = 10
  else:
    attempts = 5
  while attempts > 0:
      print(f"You have {attempts} attempts remaining to guess the number.")
      guess = int(input("Make a guess: "))
      attempts -= 1
      if guess == number:
        print(f"You got it! The answer was {guess}.")
        return
      elif guess > number and attempts !=0:
        print("Too high.")
        print("Guess again.")
      elif guess < number and attempts !=0:
        print("Too low.")
        print("Guess again.")
  if attempts == 0:
    print("You've run out of guesses. You lose.")

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1,100)
print (f"Pssst, the correct answer is {number}")
game_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
play_game(game_level)

