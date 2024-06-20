import tkinter as tk
import random

#create variables that will behave the same throughout
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50 
BODY_PARTS = 3 #how many body parts the snake has to start width 
SNAKE_COLOUR = "#00FF00"
FOOD_COLOUR = "000000"
BACKGROUND_COLOUR = "blue"

class Snake:
    pass
#create a food object 
class Food:
    def __init__(self):
        x = (random.randint(0, (GAME_WIDTH / SPACE_SIZE) - 1) * SPACE_SIZE)
        y = (random.randint(0, (GAME_HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE)
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOUR, tag='food')
        window.update()
def next_turn():
    pass

def change_direction(new_direction): #add parameters
    pass

def check_collisions():
    pass

def game_over():
    pass

#create the game window
window = tk.Tk()
window.title("Math Snake")
window.resizable(False, False)#this means the window can't be resisable by expanding by the user 

score = 0
direction = 'down'

label = tk.Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()


canvas = tk.Canvas(window, bg = BACKGROUND_COLOUR, height=GAME_HEIGHT, width=GAME_WIDTH, borderwidth = 0, highlightthickness = 0)
canvas.pack()
window.update()

#center the window
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

snake = Snake()
food = Food()



window.mainloop()

