from card import generate_card_number, generate_account_number, generate_pin
from termcolor import cprint
from collections import namedtuple
import time
from account import Accounts


class BankingSystem:
    Account = namedtuple('Account', 'id, card, pin, balance')
    CONNECTION = Accounts.CONNECTION
    CURSOR = Accounts.CURSOR

    __START_RESPONSE = {1: 'Create an account', 2: 'Log into account', 0: 'Exit'}
    __ACCOUNT_RESPONSE = {1: 'Balance', 2: 'Add Income', 3: 'Do Transfer', 4: 'Close Account', 5: 'Log Out', 0: 'Exit'}
    __WRONG_INPUT = "This option does not exist.\nPlease try again\n"

    __MAIN_MENU = 1
    __ACCOUNT_MENU = 2

    __ATTEMPTS = 0

    def __init__(self):
        self.sql = self.CURSOR.executescript('''CREATE TABLE IF NOT EXISTS CARD(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        number TEXT NOT NULL,
        pin_code TEXT NOT NULL,
        balance INTEGER NOT NULL DEFAULT 0)''')
        self.CONNECTION.commit()
        self.curr_card = None
        self.curr_pin = None
        self.state = self.__MAIN_MENU
        self.accounts = None

        self.__MAIN_ACTIONS = {1: self.new_account, 2: self.log_in, 0: self.exit}

    def start(self):
        if self.state == self.__MAIN_MENU:
            for i in self.__START_RESPONSE:
                print(f"{i}: {self.__START_RESPONSE.get(i)}", sep="\n")
        elif self.state == self.__ACCOUNT_MENU:
            for i in self.__ACCOUNT_RESPONSE:
                print(f"{i}: {self.__ACCOUNT_RESPONSE.get(i)}", sep="\n")
        return '> '

    def take_action(self, action):
        if self.check_user_input(action):
            return self.make_action(action)
        else:
            cprint(self.__WRONG_INPUT, "red")
            return self.start()

    def make_action(self, action):
        if self.state == self.__MAIN_MENU:
            self.__MAIN_ACTIONS[action]()
        elif self.state == self.__ACCOUNT_MENU:
            if action in range(4, 6):
                self.state = self.__MAIN_MENU
            elif action == 0:
                return self.exit()
            self.accounts.ACCOUNT_ACTIONS[action]()

    def check_user_input(self, action):
        if self.state == self.__MAIN_MENU:
            if action in range(0, 3):
                return True
        elif self.state == self.__ACCOUNT_MENU:
            if action in range(0, 6):
                return True
        elif action == 0:
            self.exit()
        return False

    def new_account(self):
        cprint("\n Your card has been created", 'green')
        accounts = self.get_all_accounts()
        while True:
            new_number = generate_account_number()
            card = next(generate_card_number(new_number))
            if card not in accounts.keys():
                break
        pin_code = generate_pin()
        print("\nYour card number:", card, "Your card PIN:", pin_code, sep="\n")
        self.CURSOR.execute(f'''INSERT INTO card(number, pin_code) VALUES ({card}, {pin_code})''')
        self.CONNECTION.commit()

    @staticmethod
    def get_all_accounts():
        accounts = {}
        for acc in accounts:
            accounts[acc.card] = acc.pin_code
        return accounts

    def log_in(self, card=None, pin=None, brute_force=False):
        self.dev_only_get_exists_credentials()
        if not brute_force:
            self.credentials(self.ask_card_number(), self.ask_pin_code())
        else:
            self.credentials(card, pin)
        account = self.get_account(self.curr_card, self.curr_pin)
        if account:
            self.accounts = Accounts(account)
            self.__ATTEMPTS = 0
            self.state = self.__ACCOUNT_MENU
            cprint("\n You have successfully logged in!", "green")
        else:
            self.__ATTEMPTS += 1
            if self.__ATTEMPTS >= 3:
                cprint('Sorry, hacking attempt detected. Please, wait until system will be unlocked', 'red', 'on_grey')
                time.sleep(60)
            else:
                cprint("\n Wrong card number or PIN!", 'red')

    def credentials(self, card, pin):
        self.curr_card = card
        self.curr_pin = pin

    @staticmethod
    def ask_card_number():
        print("Enter your card number:")
        user_card = int(input('> '))
        return user_card

    @staticmethod
    def ask_pin_code():
        print("Enter your PIN:")
        user_pin = int(input('> '))
        return user_pin

    def get_account(self, account_number, pin_code):
        self.CURSOR.execute(f'''SELECT * FROM card WHERE number = {account_number} AND pin_code = {pin_code}''')
        f = self.CURSOR.fetchone()
        return self.Account._make(f) if f else None

    def check_attempts(self, card):
        self.CURSOR.execute(f'''SELECT attempt FROM CARD WHERE NUMBER = {card}''')
        attempt = self.CURSOR.fetchone()
        return attempt

    def get_attempt(self, card):
        self.CURSOR.execute(f'''SELECT attempt FROM CARD WHERE NUMBER = {card}''')
        attempt = self.CURSOR.fetchone()[0]
        return attempt

    def add_attempt(self, card):
        self.CURSOR.execute(f'''UPDATE CARD SET attempt = attempt + 1 WHERE NUMBER = {card}''')
        self.CONNECTION.commit()

    def exit(self):
        print("\nBye!")
        self.CONNECTION.close()
        self.state = 'off'

    def dev_only_get_exists_credentials(self):
        """dev only part to know what credentials could be used"""
        self.CURSOR.execute('''SELECT * from card''')
        result = self.CURSOR.fetchall()
        print(result)


def main():
    bank = BankingSystem()
    response = bank.start()
    while True:
        user_input = int(input(response))
        response = bank.take_action(user_input)
        if bank.state == 'off':
            break
        elif response is None:
            response = bank.start()


if __name__ == '__main__':
    main()
