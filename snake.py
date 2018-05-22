import curses
from curses import wrapper
from random import randint

play_space_h = 20
play_space_w = 40
timer = 2000



class Snake():  # A class is needed so that we can spawn a new snake object in our game, perhaps when Life Lost?
    head = '@'  # A class variable shared by all instances
    body = 'o'
    def snake_body(self):
        body_pieces = []  # Attribute specific to this snake

def main(game_window):

    while True:
        game_window = curses.newwin(play_space_h, play_space_w)
        game_window.clear()  # Clear screen before the loop
        game_window.addstr(int(play_space_h/2), int(play_space_w/2), Snake.head)
        game_window.refresh()
        make_food(game_window)

def make_food(game_window):
    counter = 20
    game_window.box()  # Added a boarder

    while counter > 0:
        col = randint(1, play_space_w - 2)  # Needs to be -1 because of staring to count from 0
        row = randint(1, play_space_h - 2)  # Changed these so food doesn't spawn in border: 1, -2
        game_window.addstr(row, col, '#', curses.COLOR_MAGENTA)  # Terminal doesn't support colour :(
        game_window.refresh()  # Make sure that this goes before waiting for user input
        curses.beep()  # Just for fun

        # User Input testing
        key = game_window.getch()
        if key == ord('q'):
            curses.endwin() # Should go back to the terminal for timer length and then come back
        curses.napms(timer)

wrapper(main)
