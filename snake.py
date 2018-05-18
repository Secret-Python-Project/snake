import curses
from curses import wrapper


def main(game_window):
    x = 5
    timer = 1000
    welcome_message = 'Beep every: ' + str(int(timer / 1000)) + ' second/s, ' + str(x) + ' times'

    win_h, win_w = 50, 50
    game_window = curses.newwin(win_h, win_w)

    while x > 0:
        #game_window.clear()  # Clear screen
        game_window.addstr(0, 0, welcome_message, curses.A_BOLD)
        game_window.addstr(2, 0, str(str(win_h) + ' ' + str(win_w)),)  # This looks messy am I missing something????
        game_window.refresh()  # Make sure that this goes before waiting for user inPut

        curses.beep()  # Just for fun
        curses.napms(timer)
        x -= 1


wrapper(main)
