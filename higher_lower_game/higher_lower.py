from art import logo, vs
from game_data import data
import random
from replit import clear


def choice():
  """Choose a random list from the data"""
  return data[random.randint(0, len(data)-1)]

def display(choice):
  """Display the choice"""
  return f'{choice["name"]}, a {choice["description"]} from {choice["country"]} with {choice["follower_count"]}'
  

def compare(user_choice):
  """Compare the two choice and return 1 if the user wins or 0 if the user looses"""
  if user_choice == "A" and choice_A["follower_count"] > choice_B["follower_count"]:
    return 1
  elif user_choice == "B" and choice_A["follower_count"] < choice_B["follower_count"]:
    return 1
  else:
    return 0
  
  
is_game_over = False
score = 0

choice_A = choice()
choice_B = choice()

while not is_game_over:
  clear()
  print(logo)
  if score > 0:
    print(f"You're right! Current score is {score}!")
  print(f'Compare A : {display(choice_A)}')
  print(vs)
  print(f'Against B : {display(choice_B)}')
  user_choice = input('Who has more followers? Type "A" or "B" : ')
  if compare (user_choice) == 1 and choice_A != choice_B:
    score +=1  
  elif compare (user_choice) == 0 and choice_A != choice_B:
    print(f"Sorry that's wrong! Your score is {score}!")
    is_game_over = True
    
  if user_choice == "A":
    choice_A = choice()
  elif user_choice == "B":
      choice_B = choice()

