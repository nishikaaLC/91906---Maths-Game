'''This is a program that will enhance the mathematical skills of students, while having an enjoyable experience'''

#Created by Nishikaa Thakkar
#Date: 13/03/24 
from tkinter import *
import random
import tkinter as tk
from tkinter import messagebox, font

# Constants for the game settings
# The initial direction of the snake 
DIRECTION = 'down'
# Height of the game window in pixels
GAME_HEIGHT = 500
# Width of the game window in pixels 
GAME_WIDTH = 700
# Speed of the snake in milliseconds
SPEED = 130
# Size of each segment of the snake and food
SPACE_SIZE = 50
# Initial number of segments in the snake
BODY_PARTS = 2
# Colour of the snake 
SNAKE_COLOUR = 'chartreuse3'
# Background colour of the game area 
BACKGROUND_COLOUR = "RoyalBlue3"

rules_window = None
control = None
#Function to display the game rules 
def rules():
    global rules_window
    if rules_window is None or not rules_window.winfo_exists():
    #Create a new top-level window for rules
        rules_window = Toplevel()
        #Set the title of the window
        rules_window.title('RULES')
        #Set background colour of the window
        rules_window.config(bg="#a1c5ff")
        #Set the dimensions of the window
        rules_window.geometry('400x300')
        #Load the image for the icon
        snake_image = PhotoImage(file='Happy_Snake_small.png')
        #Set the icon of the window
        rules_window.iconphoto(True, snake_image)
        # Create a Text widget to display the rules
        text_widget = Text(rules_window, wrap='word', bg="#a1c5ff", font='times 10', fg="black", padx=10, pady=10)
        text_widget.pack(expand=True, fill='both')

        # Insert the rules text into the Text widget
        text_widget.insert('1.0', (
            'Welcome to Math Snake!\n\n'
            '-You need to eat the apples to grow.\n\n'
            '-If any part of your snake touches the wall or its own body, the game is over.\n\n'
            '-After eating an apple, your score will increase; however, you have to answer a simple math question correctly to continue.\n\n'
            '-Once your score reaches 20, you win!'
            '-Once you click on START LEVEL, you will be required to select a level\n\n'
            'GOOD LUCK!'
        ))
                        # Create a tag for bold and larger font
        bold_font = font.Font(weight='bold', size=14, font='times')  # Adjust size as needed
        text_widget.tag_configure('bold_large', font=bold_font)

        # Apply the tag to the first line
        text_widget.tag_add('bold_large', '1.0', '1.end')

        # Make the Text widget read-only
        text_widget.config(state='disabled')
    else:
        # Closes the rules window if it's open
        rules_window.destroy()
        rules_window = None

#Create a funtion to display the game controls 
def controls():
    global control
    if control is None or not control.winfo_exists():
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
        control.geometry('400x300')
        # Create a Text widget to display the controls
        text_widget = Text(control, wrap='word', bg="#a1c5ff", font='times 12', fg="black", padx=10, pady=10)
        text_widget.pack(expand=True, fill='both')

        # Insert the controls text into the Text widget
        text_widget.insert('1.0', (
            'How to use the program:\n\n'
            '-Use the arrow keys, or WASD keys to navigate.\n\n'
            '-Press left alt to pause and unpause.\n\n'
            '-After a collision, use the numeric keys to answer the math question.\n\n'
            '-Click Submit, or Enter to reveal if your answer was correct.'
        ))
                # Create a tag for bold and larger font
        bold_font = font.Font(weight='bold', size=14, font='consolas')  # Adjust size as needed
        text_widget.tag_configure('bold_large', font=bold_font)

        # Apply the tag to the first line
        text_widget.tag_add('bold_large', '1.0', '1.end')

        # Make the Text widget read-only
        text_widget.config(state='disabled')
    else:
        # Closes the controls window if it's open
        control.destroy()
        control = None
    
    # Create a function to set up key bindings for each window 
def setup_key_bindings(window):
    # Bind the arrow keys and WASD keys to change the snake's direction
    window.bind("<Left>", lambda event: change_direction('left'))
    window.bind("<Right>", lambda event: change_direction('right'))
    window.bind("<Up>", lambda event: change_direction('up'))
    window.bind("<Down>", lambda event: change_direction('down'))
    window.bind("<a>", lambda event: change_direction('left'))
    window.bind("<d>", lambda event: change_direction('right'))
    window.bind("<w>", lambda event: change_direction('up'))
    window.bind("<s>", lambda event: change_direction('down'))
# Function to disable the key bindings when the game is over
def disable_key_bindings(window):
    # Disable the keys to prevent direction change when the game is over
    window.bind("<Left>", lambda event: None)
    window.bind("<Right>", lambda event: None)
    window.bind("<Up>", lambda event: None)
    window.bind("<Down>", lambda event: None)
    window.bind("<a>", lambda event: None)
    window.bind("<d>", lambda event: None)
    window.bind("<w>", lambda event: None)
    window.bind("<s>", lambda event: None)
# Function to enable the key bindings when the game is over
def enable_key_bindings(window):
    setup_key_bindings(window) 
# This function will check if the snake collides with the boundaries or itself
def check_collisions(snake):
    x, y = snake.coordinates[0]
    # Check if the snake has hit the boundary
    if x < 0 or x >= GAME_WIDTH:
        return True
    elif y < 0 or y >= GAME_HEIGHT:
        return True
    # Check if the snake has collided with itself
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True
# This function will change the direction of the snake 
def change_direction(new_direction):
    global direction
    # Change the direction if it is not directly opposite to the current direction
    if direction == "left" and new_direction != "right":
        direction = new_direction
    elif direction == "right" and new_direction != "left":
        direction = new_direction
    elif direction == "up" and new_direction != "down":
        direction = new_direction
    elif direction == "down" and new_direction != "up":
        direction = new_direction
# This function will start the game when user clicks on intermediate difficulty
def start_game_intermediate():
    # This function will handle the next turn of the snake 
    def next_turn(snake, food):
        global score, SPEED
        x, y = snake.coordinates[0]
        # Update the snake's position based on its current direction
        if direction == 'up':
            y -= SPACE_SIZE
        elif direction == 'down':
            y += SPACE_SIZE
        elif direction == 'left':
            x -= SPACE_SIZE
        elif direction == 'right':
            x += SPACE_SIZE
        # Insert a new position for the snake head 
        snake.coordinates.insert(0, (x, y))
        # Create a new segment for the snake
        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR)
        snake.squares.insert(0, square)
        # Check if the snake has eaten the food
        if x == food.coordinates[0] and y == food.coordinates[1]:
            score += 1
            if label:
                label.config(text="Score: {}".format(score))
            # Remove the old food and create new food 
            canvas.delete("food")
            # Create new food with a new position
            food = Food()
            # Ask user a math question to proceed 
            ask_math_question()
            # Check for win condition
            if score >= 15:
                game_win()
                return
        else:
            del snake.coordinates[-1]
            canvas.delete(snake.squares[-1])
            del snake.squares[-1]
        # End the game if snake collides with itself 
        if check_collisions(snake):
            game_over()
        else:
            # Keep the New Game button disabled while the snake is moving
            button.config(state="disabled", bg="red")
            window.after(SPEED, next_turn, snake, food)
    def game_win():
        # Deleting all snake parts
        while snake.squares:
            canvas.delete(snake.squares.pop())
        canvas.delete(ALL)
        button.config(state="active", bg="lime")
        canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=("times", 70), text="YOU WIN!", fill="lime", tag="gamewin")
        with open('Score.txt', 'w') as f:
            f.write(f"Hello!")
            f.write(f"Congratulations! You've won the game!\n")
            f.write(f"Final Score: {score}\n")
        disable_key_bindings(window)
        level.destroy()
        window.lift()  # Bring the snake game window to the front    
        home.deiconify()  # Show the home window
        home.attributes('-topmost', False)  # Ensure home window is not on top
        home.lower()  # Send home window to the back
    def game_over():
            # Deleting all snake parts
        while snake.squares:
            canvas.delete(snake.squares.pop())
        canvas.delete(ALL)
        button.config(state="active", bg="lime")
        canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=("times", 70), text="GAME OVER!", fill="red", tag="gameover")
        #Write score to a data file once snake dies
        with open ('Score.txt', 'w') as f:
            f.write(f"Hello!")
            f.write(f" Below is your final score for the last round you played:\n")
            f.write(f"        \n")
            f.write(f" Final Score: {score}\n")
        disable_key_bindings(window)
        level.destroy()
        window.lift()  # Bring the snake game window to the front    
        home.deiconify()  # Show the home window
        home.attributes('-topmost', False)  # Ensure home window is not on top
        home.lower()  # Send home window to the back

    # Function to map numbers to their Unicode superscripts
    def to_superscript(n):
        superscripts = {
            0: '⁰', 1: '¹', 2: '²', 3: '³', 4: '⁴', 5: '⁵', 6: '⁶', 7: '⁷', 8: '⁸', 9: '⁹'
        }
        return ''.join(superscripts.get(int(digit), '') for digit in str(n))

    def ask_math_question():
        # Define a list of exponent problems with their corresponding solutions
        exponent_problems = [
            {
                "question": "{num1} to the power of {num2}?",
                "solution": lambda num1, num2: num1 ** num2
            }
        ]

        # Randomly select an exponent problem
        problem = random.choice(exponent_problems)
        
        # Generate random base and exponent
        num1 = random.randint(2, 10)  # base between 2 and 10
        num2 = random.randint(1, 3)   # exponent between 1 and 3

        # Format the question with the generated numbers and superscript for the exponent
        superscript_exponent = to_superscript(num2)
        question = f" What is {num1}{superscript_exponent} ?"
        answer = problem["solution"](num1, num2)

        # Ask the user the question and get their answer
        user_answer = f"What is {question}"
        

        def on_answer(event=None):
            user_answer = entry.get().strip()

            # Check if the input is blank
            if not user_answer:
                home.withdraw()
                level.destroy()
                messagebox.showerror("Error", "Answer cannot be blank.")
                return

            # Attempt to convert the input to an integer
            try:
                user_answer_int = int(user_answer)
            except ValueError:
                home.withdraw()
                level.destroy()
                messagebox.showerror("Error", "Please enter a valid numeric value.\n No letters or symbols.")
                return

            # Check if the answer exceeds the maximum allowed value
            if not (user_answer_int <= 99999):
                home.withdraw()
                level.destroy()
                messagebox.showerror("Error", "Answer cannot be more than 5 digits.")
                top.lower()

            # Check if the converted answer matches the expected answer
            if user_answer_int == answer:
                top.destroy()
                home.withdraw()
                level.destroy()
            else:
                messagebox.showerror("Wrong", f"Answer was {answer}! Game Over.")
                game_over()
                top.destroy()
                window.lift()  # Bring the snake game window to the front
                home.deiconify()  # Show the home window
                home.attributes('-topmost', False)  # Ensure home window is not on top
                home.lower()  # Send home window to the back
        def on_close(event=None):
            top.destroy()
            game_over()

        # Create the Toplevel window
        top = tk.Toplevel(window)
        top.title("Math Question")
        top.config(bg="#a1c5ff")

        # Calculate the position to center the Toplevel window
        window_width = window.winfo_width()
        window_height = window.winfo_height()
        top_width = 400
        top_height = 200

        x = window.winfo_x() + (window_width // 2) - (top_width // 2)
        y = window.winfo_y() + (window_height // 2) - (top_height // 2)

        top.geometry(f"{top_width}x{top_height}+{x}+{y}")


        # Create widgets for the Toplevel window
        tk.Label(top, text=question, font=("times", 14), bg="#a1c5ff").pack(pady=10)

        entry = tk.Entry(top, font=("times", 14))
        entry.pack(pady=10)
        entry.focus_set()

        entry.bind('<Return>', on_answer)

        tk.Button(top, text="Submit", font=("gameplay", 10),bg='blue',fg='cyan2',bd=6, highlightbackground='black',activebackground="darkblue",activeforeground="cyan",relief="ridge", command=on_answer).pack(side=tk.RIGHT, padx=20, pady=10)
        tk.Button(top, text="Cancel", font=("gameplay", 10),bg='blue',fg='cyan2',bd=6, highlightbackground='black',activebackground="darkblue",activeforeground="cyan",relief="ridge", command=lambda: (top.destroy(), game_over())).pack(side=tk.LEFT, padx=20, pady=10)
        top.protocol("WM_DELETE_WINDOW", on_close)
        # Wait for the math question window to close
        top.wait_window()


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
        window.lift()
        next_turn(snake, food)
        
        button.config(state="disabled", bg="red")
        enable_key_bindings(window)
    # Create the initial game window 
    global score, label, button, canvas, direction, window

    score = 0
    window = Toplevel()
    window.title("Snake Game")
    window.lift()
    direction = "down"
    label = Label(window, text="Score: {}".format(score), font=("times", 40), fg='RoyalBlue3')
    label.pack()

    paused = False
    button = Button(window, text="New Game", fg='black', font=("times", 20), command=new_game, state="disabled", bg='red', activeforeground="black",bd=5, highlightbackground='black',relief='ridge')
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

    setup_key_bindings(window)

    snake = Snake()
    food = Food()

    next_turn(snake, food)
    #This function will start the game when user clicks on advanced difficulty
def start_game_advanced():
    # This function will handle the next turn of the snake 
    def next_turn(snake, food):
        global score, SPEED
        x, y = snake.coordinates[0]
        # Update the snake's position based on its current direction
        if direction == 'up':
            y -= SPACE_SIZE
        elif direction == 'down':
            y += SPACE_SIZE
        elif direction == 'left':
            x -= SPACE_SIZE
        elif direction == 'right':
            x += SPACE_SIZE
        snake.coordinates.insert(0, (x, y))
        # Create a new segment for the snake
        square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR)
        snake.squares.insert(0, square)

        if x == food.coordinates[0] and y == food.coordinates[1]:
            score += 1
            if label:
                label.config(text="Score: {}".format(score))
            canvas.delete("food")
            food = Food()  # Create new food with a new position and image
            ask_math_question()
            # Check for win condition
            if score >= 15:
                game_win()
                return
        else:
            del snake.coordinates[-1]
            canvas.delete(snake.squares[-1])
            del snake.squares[-1]

        if check_collisions(snake):
            game_over()
        else:
            # Keep the New Game button disabled while the snake is moving
            button.config(state="disabled", bg="red")
            window.after(SPEED, next_turn, snake, food)
    def game_win():
        # Deleting all snake parts
        while snake.squares:
            canvas.delete(snake.squares.pop())
        canvas.delete(ALL)
        button.config(state="active", bg="lime")
        canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=("consolas", 70), text="YOU WIN!", fill="lime", tag="gamewin")
        with open('Score.txt', 'w') as f:
            f.write(f"Hello!")
            f.write(f"Congratulations! You've won the game!\n")
            f.write(f"Final Score: {score}\n")
        disable_key_bindings(window)
        level.destroy()
        window.lift()  # Bring the snake game window to the front    
        home.deiconify()  # Show the home window
        home.attributes('-topmost', False)  # Ensure home window is not on top
        home.lower()  # Send home window to the back
    def game_over():
            # Deleting all snake parts
        while snake.squares:
            canvas.delete(snake.squares.pop())
        canvas.delete(ALL)
        button.config(state="active", bg="lime")
        canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=("consolas", 70), text="GAME OVER", fill="red", tag="gameover")
        with open ('Score.txt', 'w') as f:
            f.write(f" Hello!\n")
            f.write(f" Below is your final score for the last round you played:\n")
            f.write(f"        \n")
            f.write(f" Final Score: {score}\n")
        disable_key_bindings(window)
        level.destroy()
        window.lift()  # Bring the snake game window to the front    
        home.deiconify()  # Show the home window
        home.attributes('-topmost', False)  # Ensure home window is not on top
        home.lower()  # Send home window to the back

    def ask_math_question():
        def generate_linear_equation():
            """Generates a simple linear algebra problem with an integer solution."""
            a = random.randint(1, 10)  # Coefficient of x
            b = random.randint(-10, 10)  # Constant term

            # Ensure the solution is an integer
            x = random.randint(-10, 10)  # Random integer solution for x
            c = a * x + b  # Calculate c to ensure that x is a solution

            # Create the equation in the form ax + b = c
            equation = f"{a}x + {b} = {c}"
            solution = x  # Solution to the equation

            return equation, solution

        def ask_linear_question():
            equation, solution = generate_linear_equation()
            question = f"Solve for x: {equation}"
            global answer
            answer = solution  # Set the correct answer
                
            def on_answer(event=None):
                user_answer = entry.get().strip()

                # Check if the input is blank
                if not user_answer:
                    home.withdraw()
                    level.destroy()
                    tk.messagebox.showerror("Error", "Answer cannot be blank.")
                    return

                # Attempt to convert the input to an integer
                try:
                    user_answer_int = int(user_answer)
                except ValueError:
                    home.withdraw()
                    level.destroy()
                    messagebox.showerror("Error", "Please enter a valid numeric value.\n No letters or symbols.")
                    return

                # Check if the answer exceeds the maximum allowed value
                if not (user_answer_int <= 99999):
                    home.withdraw()
                    level.destroy()
                    messagebox.showerror("Error", "Answer cannot be more than 5 digits.")
                    top.lower()
                    return

                # Check if the converted answer matches the expected answer
                if user_answer_int == answer:
                    top.destroy()# Close the math question window
                    home.withdraw()
                    level.destroy()
                else:
                    messagebox.showerror("Wrong", f"Answer was {answer}! Game Over.")
                    game_over()
                    top.destroy()
                    window.lift()  # Bring the snake game window to the front
                    home.deiconify()  # Show the home window
                    home.attributes('-topmost', False)  # Ensure home window is not on top
                    home.lower()  # Send home window to the back

            def on_close(event=None):
                top.destroy()
                game_over()

            # Create the Toplevel window
            top = tk.Toplevel(window)
            top.title("Math Question")
            top.config(bg="#a1c5ff")

            # Calculate the position to center the Toplevel window
            window_width = window.winfo_width()
            window_height = window.winfo_height()
            top_width = 400
            top_height = 200

            x = window.winfo_x() + (window_width // 2) - (top_width // 2)
            y = window.winfo_y() + (window_height // 2) - (top_height // 2)

            top.geometry(f"{top_width}x{top_height}+{x}+{y}")

            # Create widgets for the Toplevel window
            tk.Label(top, text=question, font=("times", 14), bg="#a1c5ff").pack(pady=10)

            entry = tk.Entry(top, font=("times", 14))
            entry.pack(pady=10)
            entry.focus_set()

            entry.bind('<Return>', on_answer)
            tk.Button(top, text="Submit", font=("gameplay", 10),bg='blue',fg='cyan2',bd=6, highlightbackground='black',activebackground="darkblue",activeforeground="cyan",relief="ridge", command=on_answer).pack(side=tk.RIGHT, padx=20, pady=10)
            tk.Button(top, text="Cancel", font=("gameplay", 10),bg='blue',fg='cyan2',bd=6, highlightbackground='black',activebackground="darkblue",activeforeground="cyan",relief="ridge", command=lambda: (top.destroy(), game_over())).pack(side=tk.LEFT, padx=20, pady=10)
            top.protocol("WM_DELETE_WINDOW", on_close)

            # Wait for the math question window to close
            top.wait_window()

        # Call the function to ask a linear algebra question
        ask_linear_question() 

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
        window.lift()
        next_turn(snake, food)
        
        button.config(state="disabled", bg="red")
        enable_key_bindings(window)    
    global score, label, button, canvas, direction, window

    score = 0
    window = Toplevel()
    window.title("Snake Game")
    window.lift()
    direction = "down"
    label = Label(window, text="Score: {}".format(score), font=("times", 40), fg='RoyalBLue3')
    label.pack()

    paused = False
    button = Button(window, text="New Game", fg='black', font=("times", 20), command=new_game, state="disabled", bg='red', activeforeground="black",bd=5, highlightbackground='black',relief='ridge')
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

    setup_key_bindings(window)
    
    snake = Snake()
    food = Food()

    next_turn(snake, food)
def start_game():
    global home, level, window
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
            # Check for win condition
            if score >= 15:
                game_win()
                return
        else:
            del snake.coordinates[-1]
            canvas.delete(snake.squares[-1])
            del snake.squares[-1]
      
        if check_collisions(snake):
            game_over()
        else:
            # Keep the New Game button disabled while the snake is moving
            button.config(state="disabled", bg="red")
            window.after(SPEED, next_turn, snake, food)
    def game_win():
        # Deleting all snake parts
        while snake.squares:
            canvas.delete(snake.squares.pop())
        canvas.delete(ALL)
        button.config(state="active", bg="lime")
        canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=("times", 70), text="YOU WIN!", fill="lime", tag="gamewin")
        with open('Score.txt', 'w') as f:
            f.write(f"Hello!")
            f.write(f"Congratulations! You've won the game!\n")
            f.write(f"Final Score: {score}\n")
        disable_key_bindings(window)
        level.destroy()
        window.lift()  # Bring the snake game window to the front    
        home.deiconify()  # Show the home window
        home.attributes('-topmost', False)  # Ensure home window is not on top
        home.lower()  # Send home window to the back


    def game_over():
            # Deleting all snake parts
        while snake.squares:
            canvas.delete(snake.squares.pop())
        canvas.delete(ALL)
        button.config(state="active", bg="lime")
        canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=("times", 70), text="GAME OVER", fill="red", tag="gameover")
        with open ('Score.txt', 'w') as f:
            f.write(f" Hello!")
            f.write(f" Below is your final score for the last round you played:\n")
            f.write(f"        \n")
            f.write(f" Final Score: {score}\n")
        disable_key_bindings(window)
        level.destroy()
        window.lift()  # Bring the snake game window to the front    
        home.deiconify()  # Show the home window
        home.attributes('-topmost', False)  # Ensure home window is not on top
        home.lower()  # Send home window to the back

    def ask_math_question():
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operator = random.choice(['+', '-', '*'])
        question = f"What is {num1} {operator} {num2}?"
        answer = eval(f"{num1}{operator}{num2}")

        def on_answer(event=None):
            user_answer = entry.get().strip()
            # Check if the input is blank
            if not user_answer:
                home.withdraw()
                level.destroy()
                tk.messagebox.showerror("Error", "Answer cannot be blank.")
                return

            # Attempt to convert the input to an integer
            try:
                user_answer_int = int(user_answer)
            except ValueError:
                home.withdraw()
                level.destroy()
                messagebox.showerror("Error", "Please enter a valid numeric value.\n No letters or symbols.")
                return

            # Check if the answer exceeds the maximum allowed value
            if not (user_answer_int <= 99999):
                home.withdraw()
                level.destroy()
                messagebox.showerror("Error", "Answer cannot be more than 5 digits.")
                top.lower()
                return

            # Check if the converted answer matches the expected answer
            if user_answer_int == answer:
                top.destroy()
                home.withdraw()
                level.destroy()
            else:
                messagebox.showerror("Wrong", f"Answer was {answer}! Game Over.")
                game_over()
                top.destroy()
                window.lift()  # Bring the snake game window to the front
                home.attributes('-topmost', False)  # Ensure home window is not on top
                home.deiconify()  # Show the home window
                home.lower()  # Send home window to the back
        def on_close(event=None):
            top.destroy()
            game_over()
      
        # Create the Toplevel window
        top = tk.Toplevel(window)
        top.title("Math Question")
        top.config(bg="#a1c5ff")
        # Calculate the position to center the Toplevel window
        window_width = window.winfo_width()
        window_height = window.winfo_height()
        top_width = 400
        top_height = 200

        x = window.winfo_x() + (window_width // 2) - (top_width // 2)
        y = window.winfo_y() + (window_height // 2) - (top_height // 2)

        top.geometry(f"{top_width}x{top_height}+{x}+{y}")

        # Create widgets for the Toplevel window
        tk.Label(top, text=question, font=("times", 14), bg="#a1c5ff").pack(pady=10)

        entry = tk.Entry(top, font=("times", 14))
        entry.pack(pady=10)
        entry.focus_set()

        entry.bind('<Return>', on_answer)

        tk.Button(top, text="Submit", font=("gameplay", 10),bg='blue',fg='cyan2',bd=6, highlightbackground='black',activebackground="darkblue",activeforeground="cyan",relief="ridge", command=on_answer).pack(side=tk.RIGHT, padx=20, pady=10)
        tk.Button(top, text="Cancel", font=("gameplay", 10),bg='blue',fg='cyan2',bd=6, highlightbackground='black',activebackground="darkblue",activeforeground="cyan",relief="ridge",command=lambda: (top.destroy(), game_over())).pack(side=tk.LEFT, padx=20, pady=10)
        top.protocol("WM_DELETE_WINDOW", on_close)

        # Be able to click submit with enter 
        # Wait for the math question window to close
        # Wait for the math question window to close
        top.wait_window()


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
        window.lift()
        next_turn(snake, food)
        
        button.config(state="disabled", bg="red")
        enable_key_bindings(window)    
    global score, label, button, canvas, direction, window

    score = 0
    window = Toplevel()
    window.title("Snake Game")
    window.lift()
    #window.resizable(False,False)             

    direction = "down"
    label = Label(window, text="Score: {}".format(score), font=("times", 40), fg='RoyalBlue3')
    label.pack()

    paused = False
    button = Button(window, text="New Game", fg='black', font=("gameplay", 20), command=new_game, state="disabled", bg='red', activeforeground="black",bd=5, highlightbackground='black',relief='ridge')
    button.pack()
    
    canvas = Canvas(window, bg=BACKGROUND_COLOUR, height=GAME_HEIGHT, width=GAME_WIDTH)
    canvas.pack(fill="both", expand=True)
    #brick_image = PhotoImage(file='Brick_Wall.png')
    window.update()
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    setup_key_bindings(window)
    
    snake = Snake()
    food = Food()

    next_turn(snake, food)

def difficulty():
    global level
    # Create a new top-level window for selecting game difficulty
    level = Toplevel()
    # Set the window title 
    level.title('Pick Level')
    # Set the background colour of the window 
    level.config(bg="#a1c5ff")
    level.attributes('-topmost', False)  # Make sure it stays behind
    level.resizable(False,False)
    # Load and set an image for the window icon
    snake_image3 = PhotoImage(file='Happy_Snake_small.png')
    level.iconphoto(True, snake_image3)
    # Set the dimensions of the window 
    level.geometry('500x200')
    # Create a label with instructions
    label = Label(level, font='consolas 10 bold', bg="#a1c5ff",fg='blue2', text=('Please select a level to start the game'))
    label.pack(pady=10)
    # Create buttons which starts the game at different difficulty levels
    beginner_btn = Button(level, text='Beginner', bg="blue", fg="cyan2", font=('gameplay', 10), command=start_game,bd=6, highlightbackground='black',activebackground="darkblue",activeforeground="cyan",relief="ridge")
    beginner_btn.pack(anchor='center', padx=10, pady=5)
    intermediate_btn = Button(level, text='Intermediate', bg="blue", fg="cyan2", font=('gameplay', 10), command=start_game_intermediate,bd=6, highlightbackground='black',activebackground="darkblue",activeforeground="cyan",relief="ridge")
    intermediate_btn.pack(anchor='center', padx=10, pady=5)
    advanced_btn = Button(level, text='Advanced', bg="blue", fg="cyan2", font=('gameplay', 10), command=start_game_advanced,bd=6, highlightbackground='black',activebackground="darkblue",activeforeground="cyan",relief="ridge")
    advanced_btn.pack(anchor='center', padx=10, pady=5)
    # Set up key bindings so the snake can move with arrow and WASD keys when button clicked
    level.bind("<Left>", lambda event: change_direction('left'))
    level.bind("<Right>", lambda event: change_direction('right'))
    level.bind("<Up>", lambda event: change_direction('up'))
    level.bind("<Down>", lambda event: change_direction('down'))
    level.bind("<a>", lambda event: change_direction('left'))
    level.bind("<d>", lambda event: change_direction('right'))
    level.bind("<w>", lambda event: change_direction('up'))
    level.bind("<s>", lambda event: change_direction('down'))
    return level

# Create the main window       
home = Tk()
# Create the title of the main window 
home.title('Math Snake')
# Create a snake image for the icon and to display on the window 
snake_image5 = PhotoImage(file='Happy_Snake.png')
# Create an icon 
home.iconphoto(True, snake_image5)
home.geometry('600x450')
home.resizable(False,False)
border_frame = Frame(home, bg='white', highlightbackground='blue', highlightcolor='blue', highlightthickness=5)
border_frame.pack(fill="both", expand=True, padx=5)
canvas1 = Canvas(border_frame, bg="#a1c5ff", width=800, height=800)
canvas1.pack(fill="both", expand=True)
canvas1.create_image(165, 10, image=snake_image5, anchor="nw")
math_image = PhotoImage(file='maths_symbols.png')
canvas1.create_image(25,230, image=math_image, anchor="nw")
startgame_btn = Button(home, text='START GAME', bg="blue", fg="cyan2", font=('gameplay', 10), command=difficulty, bd=6, highlightbackground='black',activebackground="darkblue",activeforeground="cyan",relief="ridge")
startgame_btn.place(x=50, y=50)
welcome = Label(home, font='times 15 bold ', bg="#a1c5ff", fg="blue", text=('Welcome to Math Snake!'))
welcome.place(x=25,y=10)
rules_btn = Button(home, text='RULES', bg="blue", fg="cyan2", font=('gameplay', 10), command=rules, bd=6, highlightbackground='black',activebackground="darkblue",activeforeground="cyan",relief="ridge")
rules_btn.place(x=50, y=100)

controls_btn = Button(home, text='CONTROLS', bg="blue", fg="cyan2", font=('gameplay', 10), command=controls,bd=6, highlightbackground='black',activebackground="darkblue",activeforeground="cyan",relief="ridge")
controls_btn.place(x=50, y=150)
home.mainloop()

