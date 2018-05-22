import curses
from curses import wrapper
from random import randint

play_space_h = 20
play_space_w = 40
timer = 2000


class Snake():  # A class is needed so that we can spawn a new snake object in our game, perhaps when Life Lost?
    head = '@'  # A class variable shared by all instances
    body = 'o'
    head_coords = int(play_space_h / 2), int(play_space_w / 2)

    def snake_body(self):
        body_pieces = []  # Attribute specific to this snake

def main(game_window):
    game_window = curses.newwin(play_space_h, play_space_w)
    game_window.clear()  # Clear screen before the loop
    while True:
        game_window.addstr(Snake.head_coords[0], Snake.head_coords[1], Snake.head)  # Inital Starting Position

        #make_food(game_window)  # Removed from running for the moment
        game_window.refresh()
        move_snake(game_window)
        curses.napms(1000) # So we can see it happening


def make_food(game_window):
    counter = 20
    game_window.box()  # Added a boarder

    while counter > 0:
        col = randint(1, play_space_w - 2)  # Needs to be -1 because of staring to count from 0
        row = randint(1, play_space_h - 2)  # Changed these so food doesn't spawn in border: 1, -2
        game_window.addstr(row, col, '#', curses.COLOR_MAGENTA)  # Terminal doesn't support colour :(
        game_window.refresh()  # Make sure that this goes before waiting for user input
        # curses.beep()  # Just for fun
        curses.napms(timer)


def move_snake(game_window):
    # User Input testing
    key = game_window.getch()
    if key == ord('w'):
        print('w pressed')# when w is pressed increase the Y co-ordinate of the snake head


wrapper(main)
