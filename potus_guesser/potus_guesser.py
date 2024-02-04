import csv
from . import ansi
import re
from getkey import getkey
from time import sleep

potus_names = []
play_again = True
hard_mode = False

def no_newline_print(str):
    print(str, end='')

class PotusName:
    def __init__(self, full_name):
        self.full_name = full_name

        # Gotta check for VB
        if full_name == 'Martin Van Buren':
            self.last_name = ' '.join(full_name.split()[-2:])
        else:
            self.last_name = full_name.split()[-1]

        self.initials = [word[0] for word in full_name.split()]

    def __repr__(self):
        return self.full_name

    def has_last_name(self, last_name):
        if last_name == '':
            return False
        pattern = r'\b' + re.escape(last_name) + r'\b'
        return bool(re.search(pattern, self.last_name.casefold()))
    
    def has_full_name(self, full_name):
        return full_name.casefold() == self.full_name.casefold()

def display_title_message():
    file = open('resources/title_message.txt', 'r')
    no_newline_print(file.read())
    file.close()

def populate_name_list(potus_names):
    file = open('resources/presidents.csv', 'r')
    csv_reader = csv.reader(file)
    # Stip header line
    next(csv_reader)
    for row in csv_reader:
        name_str = row[1]
        potus_names.append(PotusName(name_str))

def start_game(mode):
    ansi.clear_screen()
    ansi.show_cursor()
    potus_number = 1
    for potus_name in potus_names:
        guess = input(f"{potus_number}. ")
        wrong_guesses = 0
        while not (potus_name.has_last_name(guess) | potus_name.has_full_name(guess)):
            wrong_guesses += 1
            ansi.move_up(1)
            ansi.change_cursor_color('red')
            print(f"{potus_number}. {guess}")
            ansi.change_cursor_color('d')
            if wrong_guesses == 1:
                no_newline_print('Hint: has initials \"' + '.'.join(potus_name.initials) + '.\"')
            elif wrong_guesses >= 3:
                no_newline_print(potus_name)
            no_newline_print('[Press any key to continue]')
            ansi.hide_cursor()
            getkey()
            ansi.clear_line()
            ansi.show_cursor()
            ansi.move_up(1)
            ansi.clear_line()
            guess = input(f"{potus_number}. ")
        ansi.move_up(1)
        ansi.change_cursor_color('green')
        print(f"{potus_number}. {potus_name.full_name}")
        ansi.change_cursor_color('d')
        potus_number += 1
    print("Well done!")
    sleep(0.1)
    ansi.clear_screen()

def main():
    try:
        populate_name_list(potus_names)
        ansi.hide_cursor()
        ansi.clear_screen()
        display_title_message()
        sleep(1.5)
        ansi.clear_screen()
        print('Please select a game mode:\n\n[E]Z     [N]ormal     [H]ardcore')
        match getkey().casefold():
            case 'e':
                print('Starting EZ game...')
                sleep(0.5)
                start_game('EZ')
            case 'n':
                print('Starting Normal game...')
                sleep(0.5)
                start_game('Normal')
            case 'h':
                print('Starting Hardcore game...')
                sleep(0.5)
                start_game('Hardcore')

    except KeyboardInterrupt:
        print('Exiting...')
    

if __name__ == '__main__':
    main()