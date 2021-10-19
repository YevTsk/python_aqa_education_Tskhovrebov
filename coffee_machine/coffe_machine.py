# Coffee Machine Project

# 1 step На первом этапе необходимо вывести сообщения,
# которые соответствуют  этапам приготовления напитка.
def coffee_machine_steps():
    coffee_steps = '''Starting to make a coffee
Grinding coffee beans


Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!'''
    print(coffee_steps)


# step2  Считать количество кофейных напитков;
# Рассчитать количество каждого ингредиента.
# Одна чашка кофе  содержит 200 мл воды, 50 мл молока и 15 г кофейных зерен;
# Вывести обратно пользователю необходимое количество ингредиентов.
def main():
    cups = int(input('Write how many cups of coffee you will need: '))

    # One cup: 200 ml of water, 50 ml of milk, and 15 g of coffee beans
    water = 200 * cups
    milk = 50 * cups
    beans = 15 * cups

    print(f'For {cups} cups of coffee you will need:')
    print(f'{water} ml of water')
    print(f'{milk} ml of milk')
    print(f'{beans} g of coffee beans')


if __name__ == '__main__':
    main()

# # step3 Теперь необходимо проверить количество воды, молоко и кофейных зерен,
# доступных в кофемашине на данный момент.
def count(water: int, milk: int, beans: int, cups: int) -> str:
    possible = min([
        water // 200,
        milk // 50,
        beans // 15
    ])

    if possible == cups:
        message = 'Yes, I can make that amount of coffee'
    elif possible > cups:
        message = f'Yes, I can make that amount of coffee' \
                  f' (and even {possible - cups} more than that)'
    else:
        message = f'No, I can make only {possible} cups of coffee'

    return message


def main():
    water = int(input('Write how many ml of water the coffee machine has: '))
    milk = int(input('Write how many ml of milk the coffee machine has: '))
    beans = int(input('Write how many grams of coffee beans'
                      ' the coffee machine has: '))
    cups = int(input('Write how many cups of coffee you will need: '))

    print(count(water, milk, beans, cups))


if __name__ == '__main__':
    main()

# # step4 На данном этапе в вашей кофемашине будет ограниченный запас воды,
# молока, кофейных зерен и одноразовых стаканчиков.
# Также кофемашина  должна подсчитать выручку за продажу кофе.
# Таким образом, во-первых,  кофемашина должна продавать
# разные виды кофе: эспрессо, латте и капучино.
water = 1200
milk = 540
coffee_beans = 120
disposable_cups = 9
money = 550


def remaining():
    print("The coffee machine has:")
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{coffee_beans} of coffee beans")
    print(f"{disposable_cups} of disposable cups")
    print(f"{money} of money")


def buy():
    global water, milk, coffee_beans, disposable_cups, money
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    kind = int(input())
    if kind in [1, 2, 3]:
        disposable_cups -= 1
        if kind == 1:
            water -= 250
            coffee_beans -= 16
            money += 4
        elif kind == 2:
            water -= 350
            milk -= 75
            coffee_beans -= 20
            money += 7
        elif kind == 3:
            water -= 200
            milk -= 100
            coffee_beans -= 12
            money += 6


def fill():
    global water, milk, coffee_beans, disposable_cups
    print("Write how many ml of water do you want to add:")
    water += int(input())
    print("Write how many ml of milk do you want to add:")
    milk += int(input())
    print("Write how many grams of coffee beans do you want to add:")
    coffee_beans += int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    disposable_cups += int(input())


def take():
    global money
    print(f"I gave you ${money}")
    money = 0


def make_action():
    print("Write action (buy, fill, take):")
    action = input()
    if action == 'buy':
        buy()
    elif action == 'fill':
        fill()
    elif action == 'take':
        take()
    remaining()


remaining()
make_action()

# #step5 Ваша программа должна выполнять несколько действий одно за другим,
# постоянно спрашивая пользователя, какое действие он хочет выполнить.
water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
money = 550


def remaining():
    global water, milk, coffee_beans, disposable_cups, money
    print("The coffee machine has:")
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{coffee_beans} of coffee beans")
    print(f"{disposable_cups} of disposable cups")
    print(f"${money} of money")


def make_action(action_to_make):
    if action_to_make == 'buy':
        buy()
    elif action_to_make == 'fill':
        fill()
    elif action_to_make == 'take':
        take()
    elif action_to_make == 'remaining':
        remaining()


def buy():
    global water, milk, coffee_beans, disposable_cups, money
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    kind = int(input())
    if kind in [1, 2, 3]:
        disposable_cups -= 1
        if kind == 1:
            water -= 250
            coffee_beans -= 16
            money += 4
        elif kind == 2:
            water -= 350
            milk -= 75
            coffee_beans -= 20
            money += 7
        elif kind == 3:
            water -= 200
            milk -= 100
            coffee_beans -= 12
            money += 6


def make_coffee(water_req, milk_req, coffee_req, cost):
    global water, milk, coffee_beans, disposable_cups, money
    if water - water_req < 0:
        print("Sorry, not enough water!")
    elif milk - milk_req < 0:
        print("Sorry, not enough milk!")
    elif coffee_beans - coffee_req < 0:
        print("Sorry, not enough coffee beans!")
    elif disposable_cups - 1 < 0:
        print("Sorry, not enough disposable cups!")
    else:
        water -= water_req
        milk -= milk_req
        coffee_beans -= coffee_req
        money += cost
        disposable_cups -= 1
        print("I have enough resources, making you a coffee!")


def fill():
    global water, milk, coffee_beans, disposable_cups, money
    print("Write how many ml of water do you want to add:")
    water += int(input())
    print("Write how many ml of milk do you want to add:")
    milk += int(input())
    print("Write how many grams of coffee beans do you want to add:")
    coffee_beans += int(input())
    print("Write how many disposable cups do you want to add:")
    disposable_cups += int(input())


def take():
    global money
    print(f"I gave you ${money}")
    money = 0


while True:
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    if action == 'exit':
        break
    make_action(action)

#step6 На данном этапе необходимо реализовать класс,
# представляющий  кофемашину.
def ask_action():
    while True:
        answer = str(input("Write action (buy, fill, take, remaining, exit):\n"))
        return answer


def ask_type_of_coffee():
    answer = str(input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back – to main menu: \n"))
    return answer


def ask_fill_coffee(message):
    if message == 'water':
        answer = int(input('Write how many ml of water you want to add:\n'))
        return answer
    elif message == 'milk':
        answer = int(input('Write how many ml of milk you want to add:\n'))
        return answer
    elif message == 'coffee_beans':
        answer = int(input('Write how many grams of coffee beans you want to add:\n'))
        return answer
    elif message == 'cups':
        answer = int(input('Write how many disposable coffee cups you want to add:\n'))
        return answer


class CoffeeMachine:
    ESPRESSO = {'water': 250, 'milk': 0, 'coffee_beans': 16, 'cups': 1, 'money': 4}
    LATTE = {'water': 350, 'milk': 75, 'coffee_beans': 20, 'cups': 1, 'money': 7}
    CAPPUCCINO = {'water': 200, 'milk': 100, 'coffee_beans': 12, 'cups': 1, 'money': 6}

    def __init__(self, water, milk, coffee_beans, cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.cups = cups
        self.money = money

    def machine_action(self):
        action = ask_action()
        if action == 'buy':
            self.buy_drink()
        elif action == 'fill':
            self.fill_machine()
        elif action == 'take':
            self.take_money()
        elif action == 'remaining':
            self.machine_amount()
        elif action == 'exit':
            return()

    def available_ingredients(self, bought_drink):
        no_ingredients = ''
        if self.water - bought_drink['water'] < 0:
            no_ingredients = 'water'
        elif self.milk - bought_drink['milk'] < 0:
            no_ingredients = 'milk'
        elif self.coffee_beans - bought_drink['cofee_beans'] < 0:
            no_ingredients = 'coffee beans'
        elif self.cups - bought_drink['cups'] < 0:
            no_ingredients = 'cups'

        if no_ingredients != '':
            print(f'Sorry, not enough {no_ingredients}!')
            return False
        else:
            print('I have enough resources, making you a coffee!')
            return True

    def balance_calculation(self, bought_drink):
        self.water -= bought_drink['water']
        self.milk -= bought_drink['milk']
        self.coffee_beans -= bought_drink['cofee_beans']
        self.cups -= bought_drink['cups']
        self.money += bought_drink['money']

    def buy_drink(self):
        type_of_coffee = ask_type_of_coffee()
        if type_of_coffee == '1':
            if self.available_ingredients(self.espresso):
                self.balance_calculation(self.espresso)
        elif type_of_coffee == '2':
            if self.available_ingredients(self.latte):
                self.balance_calculation(self.latte)
        elif type_of_coffee == '3':
            if self.available_ingredients(self.cappuccino):
                self.balance_calculation(self.cappuccino)
        elif type_of_coffee == 'back':
            self.machine_action()

        self.machine_action()

    def fill_machine(self):
        self.water += ask_fill_coffee('water')
        self.milk += ask_fill_coffee('milk')
        self.coffee_beans += ask_fill_coffee('cofee_beans')
        self.cups += ask_fill_coffee('cups')
        self.machine_action()

    def take_money(self):
        print(f'I gave you {self.money}')
        self.money -= self.money
        self.machine_action()

    def machine_amount(self):
        print(f'The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.coffee_beans} of coffee beans')
        print(f'{self.cups} of disposable cups')
        print(f'{self.money} of money')
        self.machine_action()


Machine = CoffeeMachine(400, 540, 120, 9, 550)
print(Machine.machine_action())




