# from replit import clear
# from art import logo
# print(logo)
#HINT: You can call clear() to clear the output in the console.
final_dict_bidder = {}
def add_new_bider (name, bid_amount):
  final_dict_bidder[name] = bid_amount
  
print("Welcome to the seceret auction porgram.")
remaining_biders = True
biders = {}
while remaining_biders:
  #clear()
  name = input("What is your name ?:")
  bid_amount = int(input("What is your bid amount?: $"))
  add_new_bider(name, bid_amount)
  ctr = input("Are there anymore bidders yes/no?")
  if ctr == "no":
    remaining_biders = False
temp = 0
for key in final_dict_bidder:
  if  final_dict_bidder[key] > temp:
    temp = final_dict_bidder[key]
    winner = key
print(f"The winner is {key} with a bid of ${temp}")