class CoffeeMachine:
    waterOnHand = 400
    milkOnHand = 540
    beansOnHand = 120
    cupsOnHand = 9
    moneyOnHand = 550

    def query(self):
        keep_looping = True
        while keep_looping:
            print('Write action (buy, fill, take):')
            action = input()
            if action == 'buy' or 'fill' or 'take':
                return action
            else:
                print('Sorry that is not a valid response.')

    def print_on_hand_status(self):
        print('\nThe coffee machine has:')
        print(f'{self.waterOnHand} of water')
        print(f'{self.milkOnHand} of milk')
        print(f'{self.beansOnHand} of coffee beans')
        print(f'{self.cupsOnHand} of disposable cups')
        print(f'{self.moneyOnHand} of money \n')

    def make_cup_of_coffee(self, water, milk, beans, cost):
        if (
                self.waterOnHand >= water
                and self.beansOnHand >= beans
                and self.milkOnHand >= milk
        ):
            print('I have enough resources, making you a coffee!\n')
            self.waterOnHand -= water
            self.milkOnHand -= milk
            self.beansOnHand -= beans
            self.cupsOnHand -= 1
            self.moneyOnHand += cost
        else:
            if self.waterOnHand >= water:
                print('Sorry, not enough water!')
            elif self.beansOnHand >= beans:
                print('Sorry, not enough coffee beans!')
            elif self.milkOnHand >= milk:
                print('Sorry, not enough milk!')

    def fill(self):
        print('How many ml of water do you want to add?')
        self.waterOnHand += int(input())
        print('How many ml of milk do you want to add?')
        self.milkOnHand += int(input())
        print('How many g of coffee beans do you want to add?')
        self.beansOnHand += int(input())
        print('How many disposable cups do you want to add?')
        self.cupsOnHand += int(input())

    def take(self):
        print(f'I gave you ${self.moneyOnHand}')
        self.moneyOnHand = 0


class Coffee:

    def __init__(self, water, milk, beans, cost):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cost = cost
