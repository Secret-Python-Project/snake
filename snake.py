import curses
from curses import wrapper
from random import randint

# Game Configuration
play_space_h = 20
play_space_w = 40
timer = 2000
game_tick = 200

class Snake:  # A class is needed so that we can spawn a new snake object in our game, perhaps when Life Lost?
    head = 'O'  # A class variable shared by all instances
    body = 'o'

    START_LIVES = 5

    def __init__(self):
        self.lives = self.START_LIVES
        self.head_coords = int(play_space_h / 2), int(play_space_w / 2)
        self.head_y = self.head_coords[0]
        self.head_x = self.head_coords[1]
        self.direction = 'up'  #  Choose between default direction or none

    def set_direction(self, direction):
        self.direction = direction

    def move_snake_head(self, game_window):

        if self.direction == 'up':
            self.head_y -= 1
            print(self.direction)
            print(self.head_y)

        elif self.direction == 'down':
            self.head_y += 1
            print(self.direction)
            print(self.head_y)

        elif self.direction == 'left':
            self.head_x -= 1
            print(self.direction)
            print(self.head_x)

        elif self.direction == 'right':
            self.head_x += 1
            print(self.direction)
            print(self.head_x)

        game_window.addstr(self.head_coords[0], self.head_coords[1], self.head)

    def snake_body(self):
        body_pieces = []  # Attribute specific to this snake
        lives = 3


def play_game(main_window):
    game_window = curses.newwin(play_space_h, play_space_w)
    game_window.clear()  # Clear screen before the loop means all elements have to load in every loop Good or Bad?  a
    game_window.box()  # Added a border
    the_snake = Snake()
    game_window.addstr(the_snake.head_coords[0], the_snake.head_coords[1], the_snake.head)  # Starting position

    while True:
        the_snake.set_direction(get_user_direction(game_window))
        the_snake.move_snake_head(game_window)
        check_for_collision(game_window)
        game_window.refresh()
        # make_food(game_window)  # Removed from running for the moment
        #curses.napms(game_tick)


def make_food(game_window):
    counter = 20

    while counter > 0:
        col = randint(1, play_space_w - 2)
        row = randint(1, play_space_h - 2)  # Changed these so food doesn't spawn in border: 1, -2
        game_window.addstr(row, col, '#', curses.COLOR_MAGENTA)  # Terminal doesn't support colour :(
        game_window.refresh()  # Make sure that this goes before waiting for user input
        # curses.beep()  # Just for fun
        curses.napms(timer)


def get_user_direction(game_window):
    key = game_window.getch()

    if key == ord('w'):
        return 'up'

    elif key == ord('s'):
        return 'down'

    elif key == ord('a'):
        return 'left'

    elif key == ord('d'):
        return 'right'


def check_for_collision(game_window):  # List of death conditions
    if the_snake.head_x 0 or the_snake.head_x == play_space_w - 1 or Snake.head_y == 0 or Snake.head_y == play_space_h - 1:
        curses.endwin()
        quit()
    return # TODO make this do something


if __name__ == "__main__":
    wrapper(play_game)