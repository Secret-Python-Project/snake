import curses
from curses import wrapper
from random import randint

play_space_h = 20
play_space_w = 40
timer = 2000
game_tick = 500


class Snake():  # A class is needed so that we can spawn a new snake object in our game, perhaps when Life Lost?
    head = '@'  # A class variable shared by all instances
    body = 'o'
    lives = 3
    head_coords = int(play_space_h / 2), int(play_space_w / 2)
    head_y = head_coords[0]
    head_x = head_coords[1]

    def snake_body(self):
        body_pieces = []  # Attribute specific to this snake


def main(game_window):
    game_window = curses.newwin(play_space_h, play_space_w)

    while Snake.lives > 0:
        game_window.clear()  # Clear screen before the loop means all elements have to load in every loop Good or Bad?  a
        game_window.box()  # Added a border
        game_window.addstr(Snake.head_coords[0], Snake.head_coords[1], Snake.head)
        # make_food(game_window)  # Removed from running for the moment
        move_snake_with_user_input(game_window)


def make_food(game_window):
    counter = 20

    while counter > 0:
        col = randint(1, play_space_w - 2)
        row = randint(1, play_space_h - 2)  # Changed these so food doesn't spawn in border: 1, -2
        game_window.addstr(row, col, '#', curses.COLOR_MAGENTA)  # Terminal doesn't support colour :(
        game_window.refresh()  # Make sure that this goes before waiting for user input
        # curses.beep()  # Just for fun
        curses.napms(timer)


def move_snake_with_user_input(game_window):
    key = game_window.getch()
    valid_inputs = ['w', 'a', 's', 'd']
    if key == ord('w'):
        Snake.head_coords = [Snake.head_y -1, Snake.head_x]
        Snake.head_y -= 1
        check_for_collision(game_window)

    elif key == ord('s'):
        Snake.head_coords = [Snake.head_y + 1, Snake.head_x]
        Snake.head_y += 1
        check_for_collision(game_window)

    elif key == ord('a'):
        Snake.head_coords = [Snake.head_y, Snake.head_x - 1]
        Snake.head_x -= 1
        check_for_collision(game_window)

    elif key == ord('d'):
        Snake.head_coords = [Snake.head_y, Snake.head_x + 1]
        Snake.head_x += 1
        check_for_collision(game_window)


def check_for_collision(game_window):  # List of death conditions
    if Snake.head_x == 0 or Snake.head_x == play_space_w - 1 or Snake.head_y == 0 or Snake.head_y == play_space_h - 1:
        curses.endwin()
        quit()
    return # TODO make this do something


wrapper(main)
