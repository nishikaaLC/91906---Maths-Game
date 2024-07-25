'''This is a program that will enhance the mathematical skills of students, while having an enjoyable experience'''
#Created by Nishikaa Thakkar
#Date: 
#import time
from tkinter import *
import random
import os
from tkinter import simpledialog


GAME_HEIGHT = 700
GAME_WIDTH = 700
SPEED = 150
SPACE_SIZE = 50
BODY_PARTS = 4
SNAKE_COLOUR = 'blue'
FOOD_COLOUR = '#FF0000'
BACKGROUND_COLOUR = "green"

def rules():
    rule = Toplevel()
    rule.title('RULES')
    rule.geometry('400x400')
    snake_image = PhotoImage(file='Happy_Snake.png')
    window2 = Canvas(rule, bg='green')
    window2.pack(fill="both", expand=True)
    window2.create_image(0, 0, image=snake_image,anchor="nw")
    window2.create_text(190, 100, font='consolas 10 bold', text='Welcome to Math Snake\nYou need to eat the apple to grow\nIf any part of the snake touches the boundary or snakes body, the game is over\n\n. After a collision with an apple, you have 10 seconds to answer a simple math question correct to continue\n\n. GOOD LUCK!')
def controls():
    control =Toplevel()
    control.title('CONTROLS')
    control.config(bg="blue")
    control.geometry('500x300')
    canvas2 = Canvas(control, bg='white')
    canvas2.pack(fill="both", expand=True)
    canvas2.create_text(260, 100, font='consolas 10 bold', text=('Welcome to Math Snake\n\n. The navigation keys are up,down,right and bottom keys\n\n Press left alt to pause and unpause\n\nAfter the collison use the numeric keys to answer the math question\n\n'))
def start_game():
    def check_collisions(snake):
        x,y = snake.coordinates[0]
        if x<0 or x >= GAME_WIDTH:
            return True
        
        elif y < 0 or y >= GAME_HEIGHT:
            return True

        for body_part in snake.coordinates[1:]:
            if x == body_part[0] and y == body_part[1]:
                return True
    def change_direction(new_direction):
        global direction
        if new_direction == "left":
            if direction != "right":
                direction = new_direction
        elif new_direction == "right":
            if direction != "left":
                direction = new_direction
        elif new_direction == "up":
            if direction != "down":
                direction = new_direction
        elif new_direction == "down":
            if direction != "up":
                direction = new_direction



    class Snake:
        def __init__(self):
            self.body_size = BODY_PARTS
            self.coordinates = []
            self.squares = []

            for i in range(0,BODY_PARTS):
                self.coordinates.append([0, 0])
            for x, y in self.coordinates:
                square = canvas.create_rectangle(x, y, x+SPACE_SIZE, y+SPACE_SIZE, fill=SNAKE_COLOUR, tag="snake")
                self.squares.append(square)

    class Food:
        def __init__(self):
            x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
            y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
            self.coordinates = [x, y]
            apple_food=PhotoImage(file='Apple.png.png')
            apple_food_id = canvas.create_image(x + SPACE_SIZE // 2, y + SPACE_SIZE // 2, image=apple_food, anchor=CENTER, tag='food')

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
        snake.coordinates.insert(0,(x,y))
        
        square = canvas.create_rectangle(x,y,x+SPACE_SIZE,y+SPACE_SIZE,fill=SNAKE_COLOUR)
        snake.squares.insert(0, square)

        if x == food.coordinates[0] and y == food.coordinates[1]:
            score += 1
            label.config(text="Score:{}".format(score))
            canvas.delete("food")
            food = Food()
            ask_math_question()

        else:
            del snake.coordinates[-1]
            canvas.delete(snake.squares[-1])
            del snake.squares[-1]
        if check_collisions(snake):
            game_over()
        else:
            window.after(SPEED,next_turn,snake,food)


    def game_over():
        canvas.delete(ALL)
        button.config(state="active",bg = "lime")
        canvas.create_text(canvas.winfo_width()/2,canvas.winfo_height()/2,font=("consolas",70),text="GAME OVER",fill="red",tag = "gameover")

    def ask_math_question():
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-', '*'])
        question = f"What is {num1} {operator} {num2}?"
        answer = eval(f"{num1}{operator}{num2}")

        # Prompt the user for an answer
        user_answer = simpledialog.askinteger("Math Question", question, parent=window)

        # Check the answer
        if user_answer == answer:
            # Correct answer
            return True
        else:
            # Incorrect answer
            game_over()
            return False

    def new_game():
        BODY_PARTS = 3
        global score,squares,coordinates,direction,label
        direction = "down"
        squares = []
        score = 0
        coordinates =[]
        canvas.delete(ALL)
        label.config(text="Score:{}".format(score))
        snake = Snake()
        food = Food()
        next_turn(snake,food)
        button.config(state="disabled",bg="red")
        window.update()

    window = Tk()
    window.title("Math Snake")
    #window.iconbitmap(r'Apple.png.ico')
    window.resizable(False, False)
    #apple = PhotoImage(file=os.getcwd()+"\Apple.png.png")
    score = 0
    direction = "down"
    label = Label(window,text = "Score:{}".format(score),font=("consolas",40))
    label.pack()
    label = Label(window, font='arial 20 bold', text='You Can do This!').pack(side=BOTTOM)  # footer
    button = Button(window, text="New Game",fg='black', font=("consolas", 20), command=new_game,state="disabled",bg='red')
    button.pack()
    canvas = Canvas(window, bg = BACKGROUND_COLOUR,height = GAME_HEIGHT,width=GAME_WIDTH)
    canvas.pack()

    window.update()

    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width/2) - (window_width/2))
    y = int((screen_height/2) - (window_height/2))

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")
    window.bind("<Left>",lambda event: change_direction('left'))
    window.bind("<Right>",lambda event: change_direction('right'))
    window.bind("<Up>",lambda event: change_direction('up'))
    window.bind("<Down>",lambda event: change_direction('down'))


    snake = Snake()
    food = Food()

    next_turn(snake, food)
    window.mainloop()

home = Tk()
home.title('Math Snake')
#home.iconbitmap(r'favicon.ico')
home.geometry('500x500')
background = PhotoImage(file='Happy_Snake.png')

canvas1 = Canvas(home,bg="blue", width=400, height=400)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(0, 0, image=background, anchor="nw")
startgame_btn = Button(home, text='START GAME', fg='blue', font=('gameplay', 10), command=start_game)
startgame_btn.place(x=100, y=50)

rules_btn = Button(home, text='RULES', fg='blue', font=('gameplay', 10), command=rules)
rules_btn.place(x=100, y=100)

controls_btn = Button(home, text='CONTROLS', fg='blue', font=('gameplay', 10), command=controls)
controls_btn.place(x=100, y=150)

'''levels_btn = Button(home,text='DIFFICULTY',fg='blue',font=('gameplay',10),command=level)
levels_btn.place(x=100,y=200)'''
home.bind("<Left>", lambda event: change_direction('left'))
home.bind("<Right>", lambda event: change_direction('right'))
home.bind("<Up>", lambda event: change_direction('up'))
home.bind("<Down>", lambda event: change_direction('down'))


home.mainloop()

window.mainloop()

