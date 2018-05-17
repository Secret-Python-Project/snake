import curses

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
