import curses
import time
# from curses import wrapper

# Demonstrate that the code is actually doing something with a simple while loop
def main(stdscr):
    counter = 4
    while counter > 0:
        stdscr.clear()  # Clear screen
        print("Running some program", counter, ' left to display')# This won't be seen as computers are quick.
        print()
        time.sleep(1)  # Now we will see it!
        counter -= 1
    print('printing all done')


curses.wrapper(main)
