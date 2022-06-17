import tkinter as tk

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

class UI():
    def __init__(self) -> None:

        #Window
        self.window = tk.Tk()
        self.window.title("Rock Paper Scissors")
        self.window.config(padx=20, pady=20, bg=WINDOW_COLOR)
        
        #Canvas
        self.player_canvas = tk.Canvas(bg=PLAYER_COLOR, height=CANVAS_HEIGHT, width=CANVAS_WIDTH)
        self.player_canvas.grid(column=1,row=1, pady=CANVAS_PADDING)

        self.ai_canvas = tk.Canvas(bg=AI_COLOR, height=CANVAS_HEIGHT, width=CANVAS_WIDTH)
        self.ai_canvas.grid(column=3, row=1, pady=CANVAS_PADDING)

        self.score_canvas = tk.Canvas(bg=WINDOW_COLOR, height=CANVAS_HEIGHT, width=CANVAS_WIDTH)
        self.score_canvas.create_text(150, 150, text="0:0", font=("Arial", 30, "bold"))
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

        #Buttons
        self.rock_button = tk.Button(
            text="Rock", 
            width=BUTTON_WIDTH, 
            font=BUTTON_FONT, 
            padx=BUTTON_PADDING,
            pady=BUTTON_PADDING
            )
        self.rock_button.grid(column=1, row=2, sticky="W")

        self.paper_button = tk.Button(
            text="Paper", 
            width=BUTTON_WIDTH, 
            font=BUTTON_FONT, 
            padx=BUTTON_PADDING,
            pady=BUTTON_PADDING
            )
        self.paper_button.grid(column=2, row=2)

        self.scissors_button = tk.Button(
            text="Scissors", 
            width=BUTTON_WIDTH, 
            font=BUTTON_FONT, 
            padx=BUTTON_PADDING,
            pady=BUTTON_PADDING
            )
        self.scissors_button.grid(column=3, row=2, sticky="E")



        self.window.mainloop()