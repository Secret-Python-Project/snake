import curses
from curses import wrapper
from random import randint

# Game Configuration
play_space_h = 20
play_space_w = 40
timer = 2000
game_tick = 100

class Snake:  # A class is needed so that we can spawn a new snake object in our game, perhaps when Life Lost?
    head = 'O'  # A class variable shared by all instances
    body = 'o'

    START_LIVES = 1

    def __init__(self):
        self.lives = self.START_LIVES
        self.head_coords = int(play_space_h / 2), int(play_space_w / 2)
        self.head_y = self.head_coords[0]
        self.head_x = self.head_coords[1]
        self.direction = ''  # Choose between default direction or none

    def set_direction(self, direction):
        self.direction = direction

    def move_snake_head(self, game_window):

        if self.direction == 'up':
            self.head_y -= 1
            self.head_coords = int(self.head_y), int(self.head_x)

        elif self.direction == 'down':
            self.head_y += 1
            self.head_coords = int(self.head_y), int(self.head_x)

        elif self.direction == 'left':
            self.head_x -= 1
            self.head_coords = int(self.head_y), int(self.head_x)

         elif self.direction == 'right':
             self.head_x += 1
             self.head_coords = int(self.head_y), int(self.head_x)

    def check_for_bad_collision(self):  # List of death conditions
        if self.head_x == 0 or self.head_x == play_space_w - 1 or self.head_y == 0 or self.head_y == play_space_h - 1:
            self.lives -= 1

    def i_am_alive(self):
        if self.lives >= 1:
            return True
        else:
            return False


def end_game(game_window):
    game_window.addstr(10, 10, 'Sorry You Have Lost', curses.A_BOLD)
    game_window.refresh()
    curses.napms(5000)
    curses.endwin()
    quit()


def play_game(main_window):
    game_window = curses.newwin(play_space_h, play_space_w)
    the_snake = Snake()
    render_snake_position(the_snake, game_window)

    while the_snake.i_am_alive():
        curses.napms(game_tick)
        game_window.clear()  # Clear screen before the loop means all elements have to load in every loop Good or Bad?  a
        game_window.box()  # Added a border
        render_snake_position(the_snake, game_window)
        the_snake.set_direction(get_user_direction(game_window))
        the_snake.move_snake_head(game_window)
        the_snake.check_for_bad_collision()
        the_snake.i_am_alive()

        # make_food(game_window)  # Removed from running for the moment
        # curses.napms(game_tick)
    end_game(game_window)


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
    game_window.nodelay(1)
    key = game_window.getch()

    if key == ord('w'):
        return 'up'

    elif key == ord('s'):
        return 'down'

    elif key == ord('a'):
        return 'left'

    elif key == ord('d'):
        return 'right'


def render_snake_position(the_snake, game_window):
    game_window.addstr(the_snake.head_coords[0], the_snake.head_coords[1], the_snake.head)


if __name__ == "__main__":
    wrapper(play_game)