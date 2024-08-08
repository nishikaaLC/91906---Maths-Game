'''This is a program that will enhance the mathematical skills of students, while having an enjoyable experience'''

#Created by Nishikaa Thakkar
#Date: 
from tkinter import *
import random
from tkinter import simpledialog
#from fractions import Fraction
#Constants for the game settings
direction = 'down'
GAME_HEIGHT = 700
GAME_WIDTH = 700
SPEED = 150 #Speed of the snake's movement in milliseconds
SPACE_SIZE = 50 #Size of each segment of the snake and food
BODY_PARTS = 4 # Initial number of segments in the snake 
SNAKE_COLOUR = 'blue'
FOOD_COLOUR = '#FF0000'
BACKGROUND_COLOUR = "green"

#Function to dispaly the game rules 
def rules():
    #Create a new top-level window for rules
    rule = Toplevel()
    #Set the title of the window
    rule.title('RULES')
    #Set background colour of the window
    rule.config(bg="#a1c5ff")
    #Set the dimensions of the window
    rule.geometry('700x150')
    #Load the image for the icon
    snake_image = PhotoImage(file='Happy_Snake_small.png')
    #Set the icon of the window
    rule.iconphoto(True, snake_image)
    #Create the label with the rules of the game 
    label = Label(rule, bg="#a1c5ff", font='consolas 10 ', text=
        'Welcome to Math Snake\n\n'
        'You need to eat the apple to grow\n'
        'If any part of the snake touches the boundary or its own body, the game is over\n\n'
        'After eating an apple, you have 10 seconds to answer a simple math question correctly to continue\n\n'
        'The game will start straight away once you click start game'
        'GOOD LUCK!') #Add the label to the window
    label.pack()
#Create a funtion to display the game controls 
def controls():
    #Create a new top-level window for rules 
    control = Toplevel()
    #Set the title of the window 
    control.title('CONTROLS')
    #Set background colour of the window 
    control.config(bg="#a1c5ff")
    #Load the image for the icon
    snake_image3 = PhotoImage(file='Happy_Snake_small.png')
    #Set the icon of the window
    control.iconphoto(True, snake_image3)
    #Set the dimensions of the window
    control.geometry('500x150')
    #Create the label with the rules of the game 
    label = Label(control, font='consolas 10 ', bg="#a1c5ff", text=(
        'Welcome to Math Snake...\n\n'
        'Use the arrow keys to navigate.\n\n'
        'Press left alt to pause and unpause.\n\n'
        'After a collision, use the numeric keys to answer the math question.\n\n'
    ))
    #Add the label to the window
    label.pack()
def difficulty():
    difficulty = Toplevel()
    difficulty.title('Pick Level')
    difficulty.config(bg="#a1c5ff")
    snake_image3 = PhotoImage(file='Happy_Snake_small.png')
    difficulty.iconphoto(True, snake_image3)
    difficulty.geometry('500x150')
    label = Label(difficulty, font='consolas 10 ', bg="#a1c5ff", text=('Please select a level to start the game'))
    label.pack()
    beginner_btn = Button(difficulty, text='Beginner', bg="blue", fg="cyan2", font=('gameplay', 10), command=start_game)
    beginner_btn.pack()
    intermediate_btn = Button(difficulty, text='Intermediate', bg="blue", fg="cyan2", font=('gameplay', 10), command=start_game_intermediate)
    intermediate_btn.pack()
    advanced_btn = Button(difficulty, text='Advanced', bg="blue", fg="cyan2", font=('gameplay', 10), command=start_game_advanced)
    advanced_btn.pack()
#This function will check if the snake collides with the boundaries or itself
def check_collisions(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

def change_direction(new_direction):
    global direction
    if direction == "left" and new_direction != "right":
        direction = new_direction
    elif direction == "right" and new_direction != "left":
        direction = new_direction
    elif direction == "up" and new_direction != "down":
        direction = new_direction
    elif direction == "down" and new_direction != "up":
        direction = new_direction
def start_game_intermediate():
    def next_turn(snake, food):
        global score, SPEED
        x, y = snake.coordinates[0]
        if direction == 'up':
            y -= SPACE_SIZE
        elif direction == 'down':
            y += SPACE_SIZE
        elif direction == 'left':
            x -= SPACE_SIZE
        elif direction == 'right':
            x += SPACE_SIZE
        snake.coordinates.insert(0, (x, y))

        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR)
        snake.squares.insert(0, square)

        if x == food.coordinates[0] and y == food.coordinates[1]:
            score += 1
            if label:
                label.config(text="Score: {}".format(score))
            canvas.delete("food")
            food = Food()  # Create new food with a new position and image
            ask_math_question()
        else:
            del snake.coordinates[-1]
            canvas.delete(snake.squares[-1])
            del snake.squares[-1]

        if check_collisions(snake):
            game_over()
        else:
            window.after(SPEED, next_turn, snake, food)

    def game_over():
        canvas.delete(ALL)
        button.config(state="active", bg="lime")
        canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=("consolas", 70), text="GAME OVER", fill="red", tag="gameover")
        with open ('Score.txt', 'w') as f:
            f.write(f" Below is your final score for the last round you played:\n")
            f.write(f"        \n")
            f.write(f" Final Score: {score}\n")
    def ask_math_question():
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operator = random.choice(['+', '-', '*'])
        question = f"What is {num1} {operator} {num2}?"
        answer = eval(f"{num1}{operator}{num2}")

        user_answer = simpledialog.askinteger("Math Question", question, parent=window)

        if user_answer == answer:
            return True
        else:
            game_over()
            return False

    class Snake:
        def __init__(self):
            self.body_size = BODY_PARTS
            self.coordinates = []
            self.squares = []
            for i in range(BODY_PARTS):
                self.coordinates.append([0, 0])
            for x, y in self.coordinates:
                square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR, tag="snake")
                self.squares.append(square)

    class Food:
        def __init__(self):
            self.image = PhotoImage(file='Apple.png.png')
            x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
            self.coordinates = [x, y]
            canvas.create_image(x + SPACE_SIZE // 2, y + SPACE_SIZE // 2, image=self.image, anchor='center', tag='food')
    def new_game():
        global score, squares, coordinates, direction, label, button, canvas

        BODY_PARTS = 3
        direction = "down"
        squares = []
        score = 0
        coordinates = []

        if label:
            label.config(text="Score: {}".format(score))
        
        canvas.delete(ALL)
        label.config(text="Score: {}".format(score))
        
        snake = Snake()
        food = Food()
        next_turn(snake, food)
        
        button.config(state="disabled", bg="red")
    global score, label, button, canvas, direction, window

    score = 0
    window = Toplevel()
    window.title("Math Snake")

    direction = "down"
    label = Label(window, text="Score: {}".format(score), font=("consolas", 40))
    label.pack()

    paused = False
    button = Button(window, text="New Game", fg='black', font=("consolas", 20), command=new_game, state="disabled", bg='red', activeforeground="black")
    button.pack()

    canvas = Canvas(window, bg=BACKGROUND_COLOUR, height=GAME_HEIGHT, width=GAME_WIDTH)
    canvas.pack(fill="both", expand=True)
    window.update()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    window.bind("<Left>", lambda event: change_direction('left'))
    window.bind("<Right>", lambda event: change_direction('right'))
    window.bind("<Up>", lambda event: change_direction('up'))
    window.bind("<Down>", lambda event: change_direction('down'))

    snake = Snake()
    food = Food()

    next_turn(snake, food)
def start_game_advanced():
    def next_turn(snake, food):
        global score, SPEED
        x, y = snake.coordinates[0]
        if direction == 'up':
            y -= SPACE_SIZE
        elif direction == 'down':
            y += SPACE_SIZE
        elif direction == 'left':
            x -= SPACE_SIZE
        elif direction == 'right':
            x += SPACE_SIZE
        snake.coordinates.insert(0, (x, y))

        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR)
        snake.squares.insert(0, square)

        if x == food.coordinates[0] and y == food.coordinates[1]:
            score += 1
            if label:
                label.config(text="Score: {}".format(score))
            canvas.delete("food")
            food = Food()  # Create new food with a new position and image
            ask_math_question()
        else:
            del snake.coordinates[-1]
            canvas.delete(snake.squares[-1])
            del snake.squares[-1]

        if check_collisions(snake):
            game_over()
        else:
            window.after(SPEED, next_turn, snake, food)

    def game_over():
        canvas.delete(ALL)
        button.config(state="active", bg="lime")
        canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=("consolas", 70), text="GAME OVER", fill="red", tag="gameover")
        with open ('Score.txt', 'w') as f:
            f.write(f" Below is your final score for the last round you played:\n")
            f.write(f"        \n")
            f.write(f" Final Score: {score}\n")
    def ask_math_question():
        num1 = random.randint(1, 50)
        num2 = random.randint(1, 50)
        operator = random.choice(['+', '-', '*'])
        question = f"What is {num1} {operator} {num2}?"
        answer = eval(f"{num1}{operator}{num2}")

        user_answer = simpledialog.askinteger("Math Question", question, parent=window)

        if user_answer == answer:
            return True
        else:
            game_over()
            return False

    class Snake:
        def __init__(self):
            self.body_size = BODY_PARTS
            self.coordinates = []
            self.squares = []
            for i in range(BODY_PARTS):
                self.coordinates.append([0, 0])
            for x, y in self.coordinates:
                square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR, tag="snake")
                self.squares.append(square)

    class Food:
        def __init__(self):
            self.image = PhotoImage(file='Apple.png.png')
            x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
            self.coordinates = [x, y]
            canvas.create_image(x + SPACE_SIZE // 2, y + SPACE_SIZE // 2, image=self.image, anchor='center', tag='food')
    def new_game():
        global score, squares, coordinates, direction, label, button, canvas

        BODY_PARTS = 3
        direction = "down"
        squares = []
        score = 0
        coordinates = []

        if label:
            label.config(text="Score: {}".format(score))
        
        canvas.delete(ALL)
        label.config(text="Score: {}".format(score))
        
        snake = Snake()
        food = Food()
        next_turn(snake, food)
        
        button.config(state="disabled", bg="red")
    global score, label, button, canvas, direction, window

    score = 0
    window = Toplevel()
    window.title("Math Snake")

    direction = "down"
    label = Label(window, text="Score: {}".format(score), font=("consolas", 40))
    label.pack()

    paused = False
    button = Button(window, text="New Game", fg='black', font=("consolas", 20), command=new_game, state="disabled", bg='red', activeforeground="black")
    button.pack()

    canvas = Canvas(window, bg=BACKGROUND_COLOUR, height=GAME_HEIGHT, width=GAME_WIDTH)
    canvas.pack(fill="both", expand=True)
    window.update()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    window.bind("<Left>", lambda event: change_direction('left'))
    window.bind("<Right>", lambda event: change_direction('right'))
    window.bind("<Up>", lambda event: change_direction('up'))
    window.bind("<Down>", lambda event: change_direction('down'))

    snake = Snake()
    food = Food()

    next_turn(snake, food)
def start_game():
    def next_turn(snake, food):
        global score, SPEED
        x, y = snake.coordinates[0]
        if direction == 'up':
            y -= SPACE_SIZE
        elif direction == 'down':
            y += SPACE_SIZE
        elif direction == 'left':
            x -= SPACE_SIZE
        elif direction == 'right':
            x += SPACE_SIZE
        snake.coordinates.insert(0, (x, y))

        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR)
        snake.squares.insert(0, square)

        if x == food.coordinates[0] and y == food.coordinates[1]:
            score += 1
            if label:
                label.config(text="Score: {}".format(score))
            canvas.delete("food")
            food = Food()  # Create new food with a new position and image
            ask_math_question()
        else:
            del snake.coordinates[-1]
            canvas.delete(snake.squares[-1])
            del snake.squares[-1]

        if check_collisions(snake):
            game_over()
        else:
            window.after(SPEED, next_turn, snake, food)

    def game_over():
        canvas.delete(ALL)
        button.config(state="active", bg="lime")
        canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=("consolas", 70), text="GAME OVER", fill="red", tag="gameover")
        with open ('Score.txt', 'w') as f:
            f.write(f" Below is your final score for the last round you played:\n")
            f.write(f"        \n")
            f.write(f" Final Score: {score}\n")
    def ask_math_question():
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-', '*'])
        question = f"What is {num1} {operator} {num2}?"
        answer = eval(f"{num1}{operator}{num2}")

        user_answer = simpledialog.askinteger("Math Question", question, parent=window)

        if user_answer == answer:
            return True
        else:
            game_over()
            return False

    class Snake:
        def __init__(self):
            self.body_size = BODY_PARTS
            self.coordinates = []
            self.squares = []
            for i in range(BODY_PARTS):
                self.coordinates.append([0, 0])
            for x, y in self.coordinates:
                square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR, tag="snake")
                self.squares.append(square)

    class Food:
        def __init__(self):
            self.image = PhotoImage(file='Apple.png.png')
            x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
            self.coordinates = [x, y]
            canvas.create_image(x + SPACE_SIZE // 2, y + SPACE_SIZE // 2, image=self.image, anchor='center', tag='food')
    def new_game():
        global score, squares, coordinates, direction, label, button, canvas

        BODY_PARTS = 3
        direction = "down"
        squares = []
        score = 0
        coordinates = []

        if label:
            label.config(text="Score: {}".format(score))
        
        canvas.delete(ALL)
        label.config(text="Score: {}".format(score))
        
        snake = Snake()
        food = Food()
        next_turn(snake, food)
        
        button.config(state="disabled", bg="red")
    global score, label, button, canvas, direction, window

    score = 0
    window = Toplevel()
    window.title("Math Snake")

    direction = "down"
    label = Label(window, text="Score: {}".format(score), font=("consolas", 40))
    label.pack()

    paused = False
    button = Button(window, text="New Game", fg='black', font=("consolas", 20), command=new_game, state="disabled", bg='red', activeforeground="black")
    button.pack()

    canvas = Canvas(window, bg=BACKGROUND_COLOUR, height=GAME_HEIGHT, width=GAME_WIDTH)
    canvas.pack(fill="both", expand=True)
    window.update()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    window.bind("<Left>", lambda event: change_direction('left'))
    window.bind("<Right>", lambda event: change_direction('right'))
    window.bind("<Up>", lambda event: change_direction('up'))
    window.bind("<Down>", lambda event: change_direction('down'))

    snake = Snake()
    food = Food()

    next_turn(snake, food)
        
home = Tk()
home.title('Math Snake')
snake_image5 = PhotoImage(file='Happy_Snake_medium.png')
home.iconphoto(True, snake_image5)
home.geometry('600x450')
home.resizable(False,False)

canvas1 = Canvas(home, bg="#a1c5ff", width=800, height=800)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(165, 10, image=snake_image5, anchor="nw")
math_image = PhotoImage(file='maths_symbols.png')
canvas1.create_image(25,250, image=math_image, anchor="nw")
startgame_btn = Button(home, text='START GAME', bg="blue", fg="cyan2", font=('gameplay', 10), command=start_game)
startgame_btn.place(x=50, y=70)
welcome = Label(home, font='consolas 15 bold ', bg="#a1c5ff", fg="steel blue", text=('Welcome to Math Snake!'))
welcome.place(x=25,y=30)
#label = Label(difficulty, font='consolas 10 ', bg="#a1c5ff", text=('Please select a level to start the game'))
rules_btn = Button(home, text='RULES', bg="blue", fg="cyan2", font=('gameplay', 10), command=rules)
rules_btn.place(x=50, y=120)

controls_btn = Button(home, text='CONTROLS', bg="blue", fg="cyan2", font=('gameplay', 10), command=controls)
controls_btn.place(x=50, y=170)

#levels_btn = Button(home, text='DIFFICULTY', bg="blue", fg="cyan2", font=('gameplay', 10), command=difficulty)
#levels_btn.place(x=50, y=170)

home.bind("<Left>", lambda event: change_direction('left'))
home.bind("<Right>", lambda event: change_direction('right'))
home.bind("<Up>", lambda event: change_direction('up'))
home.bind("<Down>", lambda event: change_direction('down'))

home.mainloop()
