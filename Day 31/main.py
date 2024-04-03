
from tkinter import *
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"

# ----- UI SETUP -----
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# ----- IMAGE SETUP -----
right_image = PhotoImage(file="Day 31\\images\\right.png")
wrong_image = PhotoImage(file="Day 31\\images\\wrong.png")
front_card = PhotoImage(file="Day 31\\images\\card_front.png")
back_card = PhotoImage(file="Day 31\\images\\card_back.png")

# ----- FLASH CARD -----
flash_card = Canvas(height=526, width=800,
                    highlightthickness=0, bg=BACKGROUND_COLOR)
flash_card.create_image(400, 263, image=front_card)
flash_card.grid(row=0, column=0, columnspan=2)

# ----- BUTTONS -----
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(row=1, column=0)

wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(row=1, column=1)

# ----- LABELS -----
# website = Label(text="Website")
# website.grid(row=1, column=0)

window.mainloop()
