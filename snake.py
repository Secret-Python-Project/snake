import curses
import time
from curses import wrapper

timer = 5
welcome_message = "Welcome to SNAKE for: " + str(timer) + " seconds"


def main(stdscr):
    stdscr.clear()  # Clear screen
    stdscr.addstr(0, 0, welcome_message,
                  curses.A_BOLD)
    stdscr.refresh()  # Make sure that this goes before waiting for user inPut
    time.sleep(timer)


wrapper(main)
