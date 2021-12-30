from CoffeeMachine import CoffeeMachine
from CoffeeMachine import Coffee

coffeeMachine = CoffeeMachine()
espresso = Coffee(250, 0, 16, 4)
latte = Coffee(350, 75, 20, 7)
cappuccino = Coffee(200, 100, 12, 6)

program_run = True
while program_run:
    action = coffeeMachine.query()
    if action == 'buy':
        print('what do you want to buy? 1 - espresso, 2- latte, 3 - cappucino:')
        buy_response = input()
        if buy_response == 'back':
            buy_response = 0
        if int(buy_response) == 1:
            coffeeMachine.make_cup_of_coffee(espresso.water, espresso.milk, espresso.beans, espresso.cost)
        elif int(buy_response) == 2:
            coffeeMachine.make_cup_of_coffee(latte.water, latte.milk, latte.beans, latte.cost)
        elif int(buy_response) == 3:
            coffeeMachine.make_cup_of_coffee(cappuccino.water, cappuccino.milk, cappuccino.beans, cappuccino.cost)
        else:
            pass
    elif action == 'fill':
        coffeeMachine.fill()
    elif action == 'take':
        coffeeMachine.take()
    elif action == 'remaining':
        coffeeMachine.print_on_hand_status()
    elif action == 'exit':
        quit()
    else:
        continue
