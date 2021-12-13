# Написать на Python консольную версию Крестиков-Ноликов:
# 1. Меню (играть, просмотреть лог побед, очистить лог побед, выход).
# 2. Ведение логов побед и результатов игр с помощью logging
# (писать в терминал и файл одновременно). Пример: 12.10.2020 12:34 - Победил Вася...
# 3. В начале каждой игры необходимо запросить имена игроков и записывать в логи победы под этими именами.
# 4.
# Добавить возможность сыграть еще одну партию после победы/поражения с
# теми же игроками.
#
# 5. Код разбит на классы и методы. Отдельно реализована функция main.
# Пользовательский ввод осуществляется вне классов или главного класса.
#
# 6. В обязательном порядке используются Exceptions - можно писать и райзить свои.
# 7. Использовать функцию-декоратор для подсчета времени игры и его вывода в логах.
#
# 8. Код соответствует ранее изученному код-стайлу - проверка осуществляется с помощью pylint.


import logging
from pathlib import Path
import sys

Path("logs").mkdir(parents=True, exist_ok=True)


class Logging:
    def __init__(self, filename):
        self.logger = self.configure_logger()
        self.filename = filename

    @staticmethod
    def configure_logger():
        logger = logging.getLogger(__name__)
        file_handler = logging.FileHandler('game_log.log')
        file_handler.setLevel(logging.WARNING)
        file_format = logging.Formatter('%(asctime)s %(message)s', "%d-%b-%Y %H:%M:%S")
        file_handler.setFormatter(file_format)
        logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler(sys.stdout)

        stream_handler.setLevel(logging.WARNING)
        console_format = logging.Formatter('%(message)s')
        stream_handler.setFormatter(console_format)
        logger.addHandler(stream_handler)
        return logger

    def show_logs(self):
        try:
            with open(self.filename, "r") as log_file:
                print(log_file.read())
        except OSError:
            self.logger.critical('File not found')
        else:
            log_file.close()
        return main()

    def clear_logs(self):
        try:
            with open(self.filename, "w") as log_file:
                log_file.truncate()
        except OSError:
            self.logger.critical('File not found')
        else:
            log_file.close()
        return main()


class Game:
    def __init__(self):
        self.board = (['#'] * 10)
        self.log = Logging('game_log.log')
        self.player_names = {'X': '', 'O': ''}

    def display_board(self):
        blankboard = """
    ___________________
    |     |     |     |
    |  1  |  2  |  3  |
    |     |     |     |
    |-----------------|
    |     |     |     |
    |  4  |  5  |  6  |
    |     |     |     |
    |-----------------|
    |     |     |     |
    |  7  |  8  |  9  |
    |     |     |     |
    -------------------
    """

        for i in range(1, 10):
            if self.board[i] == 'O' or self.board[i] == 'X':
                blankboard = blankboard.replace(str(i), self.board[i])
            else:
                blankboard = blankboard.replace(str(i), ' ')
                print(blankboard)

    def player_input(self):
        while True:
            player1 = input("Please pick a marker 'X' or 'O' ")
            name1 = input('Please enter your name: ')
            name2 = input('Please enter name of the opponent: ')
            if player1.upper() == 'X':
                player2 = 'O'
                self.player_names['X'] = name1
                self.player_names['O'] = name2
                print("You've choosen " + player1 + f". {name2} will be " + player2)
                return player1.upper(), player2
            elif player1.upper() == 'O':
                player2 = 'X'
                self.player_names['O'] = name1
                self.player_names['X'] = name2
                print("You've choosen " + player1 + f". {name2} will be " + player2)
                return player1.upper(), player2
            print('Enter only X or O!!!')
            continue

    def place_marker(self, marker, position):
        self.board[position] = marker
        return self.board

    def space_check(self, position):
        return self.board[position] == '#'

    def full_board_check(self):
        return len([x for x in self.board if x == '#']) == 1

    def win_check(self, mark):
        win_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        for i in range(0, len(win_list)):
            result = all(self.board[element] == mark for element in win_list[i])
            if result:
                break
        return result

    def player_choice(self):
        while True:
            try:
                choice = input("Please select an empty space between 1 and 9 : ")
                if int(choice) < 1 or int(choice) > 9:
                    print('Enter only numbers between 1 and 9!!!')
                    continue
                if not self.space_check(int(choice)):
                    print("This space isn't free. Please choose between 1 and 9 : ")
                    continue
                else:
                    return choice
            except ValueError:
                print('Enter only numbers between 1 and 9!!!')

    # def ask_names(self):
    #     name1 = input('Your name, player 1: ')
    #     name2 = input('Your name, player 2: ')
    #     self.player_names.= name1
    #     self.player_names[1] = name2

    def play_game(self):
        # self.ask_names()
        i = 1
        players = self.player_input()
        # Empty board init
        # game_on = full_board_check(board) #пока не будет равно 1 (не будет свободных клеток
        while True:
            # Who's playing ?
            marker = players[1] if i % 2 == 0 else players[0]
            # Player to choose where to put the mark. Play !
            self.place_marker(marker, int(self.player_choice()))
            # Check the board
            self.display_board()
            i += 1
            if self.win_check(marker):
                self.log.logger.warning(f'{self.player_names[f"{marker}"]} wins')
                return
            elif self.full_board_check():
                self.log.logger.warning('Tie')
                return


def main():
    game = Game()
    options = {'1': 'Play game', '2': 'Show Logs', '3': 'Clear Logs', '0': 'Exit'}
    actions = {'1': game.play_game, '2': game.log.show_logs, '3': game.log.clear_logs, '0': exit}
    for k in options:
        print(f"{k}: {options.get(k)}", sep="\n")
    try:
        user_choice = input('> ')
        actions[user_choice]()
    except KeyError:
        print("This option does not exist.\nPlease try again")
    return main()


if __name__ == "__main__":
    print('Welcome to Tic Tac Toe!')
    main()
