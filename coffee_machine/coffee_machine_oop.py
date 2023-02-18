from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_stuff = CoffeeMaker()
money_bank = MoneyMachine()
options = Menu()
#item = MenuItem()
loop_on = True
while loop_on:
 
  user_input = input(f"What would you like ti have ? {options.get_items()} : ")
  if user_input =="off":
    loop_on = False
  elif user_input == "report":
    print(f"{coffee_stuff.report()}")
    print(f"{money_bank.report()}")
  else:
    item = options.find_drink(user_input)
    if coffee_stuff.is_resource_sufficient(item) == False:
      print("Sorry not sufficient ingredients")
    elif coffee_stuff.is_resource_sufficient(item) == True:
      money_bank.make_payment(item.cost)
      coffee_stuff.make_coffee(item)
        