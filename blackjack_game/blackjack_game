
from art import logo
import random
import os

def random_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(the_list):
  if sum(the_list) == 21 and len(the_list) == 2:
    return 0
  if sum(the_list) > 21 and 11 in the_list:
    the_list.remove(11)
    the_list.append(1)
  return sum(the_list)

def compare(user_score, computer_score):
  if computer_score == 0:
    return "you loose, computer has a blackjack"
  elif user_score == 0:
    return "You won"
  elif user_score == computer_score:
    return "Draw"
  elif user_score > 21:
    return "You loose, you went over"
  elif computer_score > 21:
    return "You win, computer went over"
  elif user_score > computer_score:
    return "You won"
  else:
    return "You loose"
  
def play_game():
  print(logo)
  user_card = []
  computer_card = []
  is_game_over = False
  for i in range(2):
    user_card.append(random_card())
    computer_card.append(random_card())
    
  while not is_game_over:
    print (f"Your cards are {user_card}")
    print (f"Computers first card is {computer_card[0]}")
    user_score = calculate_score(user_card)
    computer_score = calculate_score(computer_card)
    #print(f"{user_card} and {user_score}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_selection = input('Type "y" to pick another card type "n" to  pass: ')
      if user_selection == "y":
        user_card.append(random_card())
      if user_selection == "n":
        is_game_over = True
  
        
  while computer_score !=0 and computer_score < 17:
    computer_card.append(random_card())
    computer_score = calculate_score(computer_card)
    
  print (f"Your cards are {user_card} and your score is {user_score}")
  print (f"Computer's cards are {computer_card} and computer's score is {computer_score}")
  print(compare( user_score, computer_score))


while (input('Do you want to play a game of blackjack ? Type "y" for Yes and "n" for No : ') == "y"):
  os.system('cls')
  play_game()