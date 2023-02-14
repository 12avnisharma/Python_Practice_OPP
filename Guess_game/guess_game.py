#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
from replit import clear
import random

def play_guess():
  print(logo)
  print("Welcome to the number guessing game!")
  print("I'm thinking of a number between 1 to 100")
  difficulty_type = input("Choose a difficulty. easy or hard ? : ")
  
  computer_selected_number = random.randint(1, 100)
  #print(f"computer selected number is {computer_selected_number}")
  
  if difficulty_type == "easy":
    attempts = 10
    print("You have 10 attempts to choose the numbner!")
  else: 
    attempts = 5
    print("You have 5 attempts to choose the numbner!")
  
  for i in range (0, attempts):
    user_number = int(input("Make a guess: "))
    if user_number > computer_selected_number:
      print("Too high")
      print("guess again")
      print(f"You have {attempts - (i+1)} attempts remaining.")
    elif user_number < computer_selected_number:
      print("Too low")
      print("guess again")
      print(f"You have {attempts - (i+1)} attempts remaining.")    
    else :
      print(f"You got it! the answer was {computer_selected_number}")
      print(f"You have {attempts - (i+1)} attempts remaining.")    
  
while (input("Guess again! ? type y for yes and n for no : ") == "y"):
  clear()
  play_guess()
  