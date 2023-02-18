MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0

def check(user_input):
  for i in MENU[user_input]["ingredients"]:
    if int(MENU[user_input]["ingredients"][i]) > int(resources[i]):
      return 0
    elif int(MENU[user_input]["ingredients"][i]) <= int(resources[i]):
      return 1
def check_transaction(user_input, value):
  if float(MENU[user_input]["cost"]) >= value:
    return 0
  elif float(MENU[user_input]["cost"]) < value:
    return 1
    
def make_item(user_input):
  for i in MENU[user_input]["ingredients"]:
    resources[i] = int(resources[i]) - int(MENU[user_input]["ingredients"][i])
 ######################################################################### 
end_loop = False
while not end_loop:
  user_input  = input("What would you like? (espresso/latte/cappuccino): ")

  if user_input == "off":
    end_loop = True
  elif  user_input == "report":
    print(f'Water : {resources["water"]}ml')
    print(f'Milk : {resources["milk"]}ml')
    print(f'coffee : {resources["coffee"]}g')
    print(f'Money : ${profit}')
  elif user_input in MENU:
    if check(user_input) == 0:
      print("Sorry there is not enough ingredients")
    else:
      print("Please insert coins.")
      n_quaters = float(input("How many quaters : "))
      n_dime = float(input("How many dime : "))
      n_nickle = float(input("How many nickle : "))
      n_pennies = float(input("How many pennies : "))
      value = 0.25 * n_quaters + 0.10 * n_dime + 0.05 * n_nickle + 0.01 * n_pennies
      print(value)
      print(float(MENU[user_input]["cost"]))
      if check_transaction(user_input, value) == 0:
        print("Sorry not enough money. Money refunded")
      else:
        profit += float(MENU[user_input]["cost"]) 
        print(f'Here is ${(value - float(MENU[user_input]["cost"])): 0.2f} dollars in change.')
        make_item(user_input)
        print(f"Here's your {user_input}. Enjoy!")
        