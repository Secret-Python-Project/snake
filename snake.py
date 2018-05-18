import curses
from curses import wrapper

timer = 1000


def main(stdscr):
    x = 5
    welcome_message = 'Beep every: ' + str(int(timer / 1000)) + ' second/s, ' + str(x) + ' times'

    while x > 0:
        win_h, win_w = stdscr.getmaxyx()  # NOTE that the height and width are in columns

        stdscr.clear()  # Clear screen
        stdscr.addstr(0, 0, welcome_message, curses.A_BOLD)
        stdscr.addstr(2, 0, str(str(win_h) + ' ' + str(win_w)),)  # This looks messy am I missing something????
        stdscr.refresh()  # Make sure that this goes before waiting for user inPut

        curses.beep()  # Just for fun
        curses.napms(timer)
        x -= 1


wrapper(main)
