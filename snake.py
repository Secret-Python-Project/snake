import curses
from curses import wrapper

play_space_h = 40
play_space_w = 150
timer = 20


def main(game_window):

    game_window = curses.newwin(play_space_h, play_space_w)

    col = 0
    row = 0

    game_window.clear()  # Clear screen before the loop
    while row < play_space_h:
        while col < play_space_w:

            game_window.addstr(row, col, '@')
            game_window.refresh()  # Make sure that this goes before waiting for user inPut
            # curses.beep()  # Just for fun
            col += 1
            curses.napms(timer)
        row += 1
        col = 0


wrapper(main)
