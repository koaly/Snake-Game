import arcade
 
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
 
class SnakeWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.BLACK)
 
 
if __name__ == '__main__':
    window = SnakeWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()