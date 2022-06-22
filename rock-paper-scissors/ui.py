import tkinter as tk
from PIL import Image, ImageTk
import random as r

WINDOW_COLOR = "#DFF6FF"
CANVAS_HEIGHT = 300
CANVAS_WIDTH = 300
CANVAS_PADDING = 10
PLAYER_COLOR = "#F94C66"
AI_COLOR = "#1363DF"
BUTTON_WIDTH = 20
BUTTON_PADDING = 20
BUTTON_FONT = ("Arial", 15, "bold")
LABEL_FONT = ("Impact", 25, "bold")
ROCK_PNG = "images/rock.png"
PAPER_PNG = "images/paper.png"
SCISSORS_PNG = "images/scissors.png"
MOVES = ["rock", "paper", "scissors"]


class UI():
    def __init__(self) -> None:

        #Window
        self.window = tk.Tk()
        self.window.title("Rock Paper Scissors")
        self.window.config(padx=20, pady=20, bg=WINDOW_COLOR)

        #Moves
        self.player_choice = ""
        self.ai_choice = ""

        #Score
        self.player_score = 0
        self.ai_score = 0

        #Images
        self.rock_img = self.convert_img(ROCK_PNG)
        self.paper_img = self.convert_img(PAPER_PNG)
        self.scissors_img = self.convert_img(SCISSORS_PNG)

        self.img_dict = {
            "rock": self.rock_img,
            "paper": self.paper_img,
            "scissors": self.scissors_img
        }
        
        #Canvas
        self.player_canvas = tk.Canvas(bg=PLAYER_COLOR, height=CANVAS_HEIGHT, width=CANVAS_WIDTH)
        self.player_img = self.player_canvas.create_image(0,0,image=self.rock_img, anchor="nw")
        self.player_canvas.grid(column=1,row=1, pady=CANVAS_PADDING)

        self.ai_canvas = tk.Canvas(bg=AI_COLOR, height=CANVAS_HEIGHT, width=CANVAS_WIDTH)
        self.ai_img = self.ai_canvas.create_image(0,0,image=self.rock_img, anchor="nw")
        self.ai_canvas.grid(column=3, row=1, pady=CANVAS_PADDING)

        self.score_canvas = tk.Canvas(bg=WINDOW_COLOR, height=CANVAS_HEIGHT, width=CANVAS_WIDTH)
        self.score = self.score_canvas.create_text(
            150, 
            150, 
            text=f"{self.player_score}:{self.ai_score}", 
            font=("Arial", 30, "bold")
            )
        self.score_canvas.grid(column=2, row=1, pady=CANVAS_PADDING)

        #Labels
        self.player_label = tk.Label(
            text="Player", 
            font=LABEL_FONT, 
            highlightthickness=0, 
            bg=WINDOW_COLOR
            )
        self.player_label.grid(column=1, row=0)

        self.ai_label = tk.Label(
            text="Opponent",
            font=LABEL_FONT,
            highlightthickness=0,
            bg=WINDOW_COLOR
        )
        self.ai_label.grid(column=3, row=0)

        self.score_label = tk.Label(
            text="Score",
            font=LABEL_FONT,
            highlightthickness=0,
            bg=WINDOW_COLOR
        )
        self.score_label.grid(column=2, row=0)
        
        #Buttons
        self.rock_button = tk.Button(
            text="Rock", 
            width=BUTTON_WIDTH, 
            font=BUTTON_FONT, 
            padx=BUTTON_PADDING,
            pady=BUTTON_PADDING,
            command=self.choose_rock
            )
        self.rock_button.grid(column=1, row=2, sticky="W")

        self.paper_button = tk.Button(
            text="Paper", 
            width=BUTTON_WIDTH, 
            font=BUTTON_FONT, 
            padx=BUTTON_PADDING,
            pady=BUTTON_PADDING,
            command=self.choose_paper
            )
        self.paper_button.grid(column=2, row=2)

        self.scissors_button = tk.Button(
            text="Scissors", 
            width=BUTTON_WIDTH, 
            font=BUTTON_FONT, 
            padx=BUTTON_PADDING,
            pady=BUTTON_PADDING,
            command=self.choose_scissors
            )
        self.scissors_button.grid(column=3, row=2, sticky="E")



        self.window.mainloop()
    
    #Functions

    def convert_img(self, image):
        img = Image.open(image)
        resized_img = img.resize((CANVAS_HEIGHT,CANVAS_WIDTH), Image.ANTIALIAS)
        new_img = ImageTk.PhotoImage(resized_img)
        return new_img

    def choose_rock(self):
        self.player_canvas.itemconfig(self.player_img, image=self.rock_img)
        self.player_choice = "rock"
        self.ai_choose()
        self.update_score(self.player_choice, self.ai_choice)

    def choose_paper(self):
        self.player_canvas.itemconfig(self.player_img, image=self.paper_img)
        self.player_choice = "paper"
        self.ai_choose()
        self.update_score(self.player_choice, self.ai_choice)

    def choose_scissors(self):
        self.player_canvas.itemconfig(self.player_img, image=self.scissors_img)
        self.player_choice = "scissors"
        self.ai_choose()
        self.update_score(self.player_choice, self.ai_choice)
    
    def ai_choose(self):
        self.ai_choice = r.choice(MOVES)
        self.ai_canvas.itemconfig(self.ai_img, image=self.img_dict[self.ai_choice])
    
    def update_score(self, player_choice, ai_choice):
        if ai_choice == player_choice:
            pass
        elif player_choice == "rock":
            if ai_choice == "paper":
                self.ai_score += 1
            elif ai_choice == "scissors":
                self.player_score += 1
        elif player_choice == "paper":
            if ai_choice == "rock":
                self.player_score += 1
            elif ai_choice == "scissors":
                self.player_score += 1
        elif player_choice == "scissors":
            if ai_choice == "rock":
                self.ai_score += 1
            elif ai_choice == "paper":
                self.player_score += 1
        self.score_canvas.itemconfig(self.score, text=f"{self.player_score}:{self.ai_score}")
    
    