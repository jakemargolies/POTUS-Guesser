import time
import sys

def move_up(num_rows):
    __print_commands(f"[{num_rows}A")

def clear_screen():
    __print_commands(['[1J', '[H'])

def hide_cursor():
    __print_commands('[?25l')

def show_cursor():
    __print_commands('[?25h')

def clear_line():
    __print_commands(['[2K', '[0G'])

def change_cursor_bg_color(color):
    if color in ['green', 'Green', 'GREEN', 'g', 'G']:
        __print_commands('[48;5;42m')
    elif color in ['black', 'Black', 'B', 'b']:
        __print_commands('[48;5;49m')
    
def change_cursor_color(color):
    if color in ['green', 'Green', 'GREEN', 'g', 'G']:
        __print_commands('[32m')
    elif color in ['default', 'Default', 'D', 'd']:
        __print_commands('[0m')
    elif color in ['red', 'Red', 'RED', 'r', 'RED']:
        __print_commands('[31m')

def __print_commands(commands):
    if isinstance(commands, list):
        print('\033' + '\033'.join(commands), end='')
    else:
        print('\033' + commands, end='')
    sys.stdout.flush()
