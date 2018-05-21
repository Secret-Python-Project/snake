import curses
from curses import wrapper
from random import randint

play_space_h = 20
play_space_w = 40
timer = 250



class snake():  # A class is needed so that we can spawn a new snake object in our game.
    head = 'O'
    body = 'o'


def main(game_window):

    col = 0
    row = 0
    game_window = curses.newwin(play_space_h, play_space_w)
    game_window.clear()  # Clear screen before the loop
    game_window.addstr(int(play_space_h/2), int(play_space_w/2), 'O')
    game_window.refresh()
    curses.napms(5000)  # TODO: Remove - for Testing
    #make_food(game_window)

def make_food(game_window):
    counter = 100
    game_window.box()  # Added a boarder

    while counter > 0:
        col = randint(1, play_space_w - 2)  # Needs to be -1 because of staring to count from 0
        row = randint(1, play_space_h - 2)  # Changed these so food doesn't spawn in border.
        game_window.addstr(row, col, '#', curses.COLOR_MAGENTA)
        game_window.refresh()  # Make sure that this goes before waiting for user input
        # curses.beep()  # Just for fun
        curses.napms(timer)


wrapper(main)
