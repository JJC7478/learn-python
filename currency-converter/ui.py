from tkinter import *
from turtle import width

TITLE_BG_COLOR = "#A5BECC"
BUTTON_FONT = ("Impact", 15)
ENTRY_FONT = ("Impact", 15)
ENTRY_WIDTH = 15
BUTTON_WIDTH = 30
TITLE_FONT = ("Impact", 45, "normal")
FROM_TO_FONT = ("Impact", 25, "normal")
WINDOW_COLOR = "#53BF9D"


class UI():
    def __init__(self):

        #Window
        self.window = Tk()
        self.window.title("Conversion-tron 9000")
        self.window.minsize(width=500,height=500)
        self.window.config(bg=WINDOW_COLOR)

        #Currencies
        self.currencies = ["US Dollar", "Euro", "Japanese Yen", "British Pound", "Canadian Dollar"]
        self.option_var1 = StringVar()
        self.option_var1.set(self.currencies[0])
        self.option_var2 = StringVar()
        self.option_var2.set(self.currencies[1])

        #Labels
        self.converter_title_label = Label(text="Converter-tron 9000", font=TITLE_FONT, bg=TITLE_BG_COLOR)
        self.converter_title_label.config(padx=20,pady=20)
        self.converter_title_label.grid(column=2,row=0)

        self.from_label = Label(text="From", font=FROM_TO_FONT, padx=20,bg=WINDOW_COLOR)
        self.from_label.config(width=15)
        self.from_label.grid(column=0, row=1)

        self.to_label = Label(text="To", font=FROM_TO_FONT,bg=WINDOW_COLOR)
        self.to_label.config(width=15)
        self.to_label.grid(column=4, row=1)

        #Text Entries
        self.from_entry = Entry(width=ENTRY_WIDTH, font=ENTRY_FONT)
        self.from_entry.grid(column=0,row=2)

        self.to_entry = Entry(width=ENTRY_WIDTH, font=ENTRY_FONT)
        self.to_entry.grid(column=4, row=2)

        #Dropdown Menus
        self.from_menu = OptionMenu(
            self.window,
            self.option_var1,
            *self.currencies
        )
        self.from_menu.config(width=20, highlightthickness=0)
        self.from_menu.grid(column=0, row=3)

        self.to_menu = OptionMenu(
            self.window,
            self.option_var1,
            *self.currencies
        )
        self.to_menu.config(width=20, highlightthickness=0)
        self.to_menu.grid(column=4, row=3)

        #Buttons
        self.convert_button = Button(text="Convert", width=BUTTON_WIDTH, font=BUTTON_FONT)
        self.convert_button.grid(column=2, row=4)

        self.clear_button = Button(text="Clear",  width=BUTTON_WIDTH, font=BUTTON_FONT)
        self.clear_button.grid(column=2, row=5)







        self.window.mainloop()