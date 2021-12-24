import random


def luhn_algorithm(card_number):
    card_number = list(map(int, card_number))
    for i, _ in enumerate(card_number, 1):
        if i % 2 != 0:
            card_number[i - 1] *= 2
        if card_number[i - 1] > 9:
            card_number[i - 1] -= 9
    return sum(card_number)


def generate_card_number(acc_number):
    iin = "400000"
    luhn_sum = luhn_algorithm(iin + acc_number)
    checksum = get_checksum(luhn_sum)
    yield iin + acc_number + str(checksum)


def get_checksum(luhn_sum):
    return 10 - luhn_sum % 10 if luhn_sum % 10 != 0 else 0


def generate_account_number():
    acc_number = ""
    for _ in range(9):
        acc_number += str(random.randrange(10))
    return acc_number


def generate_pin():
    pin_code = ""
    for i in range(4):
        pin_code += str(random.randrange(10))
    return pin_code
