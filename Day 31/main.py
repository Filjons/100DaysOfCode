
from tkinter import *
from tkinter import messagebox
import pandas as pd
import random as rd
BACKGROUND_COLOR = "#B1DDC6"
DATA_FILE = "Day 31\\data\\french_words.csv"


word_list = {}

# ----- DICTIONARY -----
data_file = pd.read_csv(DATA_FILE)

word_list = data_file.to_dict(orient='records')

word = rd.choice(word_list)

def next_card():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = rd.choice(word_list)
    flash_card.itemconfig(card_title, text="French", fill="black")
    flash_card.itemconfig(card_word, text=word["French"], fill="black")
    flash_card.itemconfig(card_background, image=front_card)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    flash_card.itemconfig(card_title, text="English", fill="white")
    flash_card.itemconfig(card_word, text=word["English"], fill="white")
    flash_card.itemconfig(card_background, image=back_card)

# ----- UI SETUP -----
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# ----- IMAGE SETUP -----
right_image = PhotoImage(file="Day 31\\images\\right.png")
wrong_image = PhotoImage(file="Day 31\\images\\wrong.png")
front_card = PhotoImage(file="Day 31\\images\\card_front.png")
back_card = PhotoImage(file="Day 31\\images\\card_back.png")
cards = {front_card,back_card}

# ----- FLASH CARD -----
flash_card = Canvas(height=526, width=800,
                    highlightthickness=0, bg=BACKGROUND_COLOR)
card_background = flash_card.create_image(400, 263, image=front_card)
card_title = flash_card.create_text(
    400, 150, text="French", font=("Ariel", 40, "italic"))
card_word = flash_card.create_text(
    400, 263, text=word["French"], font=("Ariel", 60, "bold"))

flash_card.grid(row=0, column=0, columnspan=2)

# ----- BUTTONS -----
wrong_button = Button(
    image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_button = Button(
    image=right_image, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=1)

# ----- LABELS -----
# website = Label(text="Website")
# website.grid(row=1, column=0)

window.mainloop()
