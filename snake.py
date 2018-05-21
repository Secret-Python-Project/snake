import curses
from curses import wrapper
from random import randint

play_space_h = 20
play_space_w = 40
timer = 500


def main(game_window):

    game_window = curses.newwin(play_space_h, play_space_w)

    col = 0
    row = 0

    game_window.clear()  # Clear screen before the loop
    while row < play_space_h:
        while col < play_space_w:

            game_window.addstr(row, col, '$')
            game_window.refresh()  # Make sure that this goes before waiting for user inPut
            # curses.beep()  # Just for fun
            col += 1
            curses.napms(timer)
        row += 1
        col = 0


def make_food(gamewindow):
    game_window = curses.newwin(play_space_h, play_space_w)
    counter = 100

    while counter > 0:
        col = randint(0, play_space_w - 1)  # needs to be -1 because of staring to count from 0
        row = randint(0, play_space_h - 1)
        game_window.addstr(row, col, '%')
        game_window.refresh()  # Make sure that this goes before waiting for user input
        # curses.beep()  # Just for fun
        curses.napms(timer)


wrapper(make_food)
