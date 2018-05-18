import curses
# from curses import wrapper

# TODO Clean up notes and redundant code now it isn't being used.

def main(stdscr):
    # Clear screen
    stdscr.clear()
    # Proceed with your program
    print("Running some program")  # This won't be seen as computers are quick.

# wrapper is a function that does all of the setup and teardown, and makes sure
# your program cleans up properly if it errors!

curses.wrapper(main)


# curses.wrapper() turns on:
# cbreak mode,
# turns off echo,
# enables the terminal keypad,
# and initializes colors if the terminal has color support.
# On exit (whether normally or by exception) it restores:
# cooked mode,
# turns on echo,
# and disables the terminal keypad.


'''
# STANDARD CURSES SETUP:
stdscr = curses.initscr()  # Creates a new window object
curses.noecho()  # EXPLICT: do not update console with user input- it is usually ignored anyway)
curses.cbreak()  # React to key input without requiring return
stdscr.keypad(True)  # Allows special input like the arrow keys


# To stop a curses application we reverse the above with:
curses.nocbreak()
stdscr.keypad(False)
curses.echo()

curses.endwin()  #  Returns the terminal/console to normality
'''