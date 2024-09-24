import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
cancel = None
# ----------------------------NEW FLASH CARD--------------------------------#
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pd.read_csv("data/french_words.csv")


list_data = data.to_dict(orient="records")


def right():
    global list_data, current_card
    list_data.remove(current_card)

    rem_data = list_data
    df = pd.DataFrame(rem_data)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()


current_card = {}


def english():
    window.after_cancel(cancel)
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(title_card, text="English", fill="white")
    canvas.itemconfig(word_card, text=current_card["English"], fill="white")


def next_card():
    global cancel
    global current_card
    window.after_cancel(cancel)
    current_card = random.choice(list_data)
    canvas.itemconfig(title_card, text="French", fill="black")
    canvas.itemconfig(word_card, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    cancel = window.after(3000, english)


# ----------------------------UI SETUP--------------------------------#

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
cancel = window.after(3000, english)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
title_card = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_card = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Wrong Button
wr = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wr, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

# Right Button
ri = PhotoImage(file="./images/right.png")
right_button = Button(image=ri, highlightthickness=0, command=right)
right_button.grid(column=1, row=1)

next_card()

window.mainloop()
