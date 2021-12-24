from bank import BankingSystem


def brute(base, number):
    i = 0
    while i <= number:
        yield base + i
        i += 1


def main():
    bank = BankingSystem()
    card_generator = brute(400000000000000, 999999999)
    pin_generator = brute(0, 9999)
    while True:
        card = str(next(card_generator))
        while True:
            pin = str(next(pin_generator, "last_pin"))
            if pin == "last_pin":
                pin_generator = brute(0, 9999)
                break
            if len(pin) == 1:
                pin = "000" + pin
            elif len(pin) == 2:
                pin = "00" + pin
            elif len(pin) == 3:
                pin = "0" + pin
            print(f'''Brute forced with:
            Card: {card}
            Pin_code: {pin}''')
            if bank.log_in(card, pin, brute_force=True):
                hacked = "You're hacked!"
                print(hacked)
                exit()


if __name__ == '__main__':
    main()
    