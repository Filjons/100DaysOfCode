from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    #If it's the 1sth or other rep
    count_down(work_sec)
    #If it's the 8th rep
    count_down(long_break_sec)
    #If it's the 2nd or something rep
    count_down(short_break_sec)
    
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        window.after(1000, count_down, count -1)
    

# ---------------------------- UI SETUP ------------------------------- #
        
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

title_label = Label(text="Timer", font=(FONT_NAME, 45, "bold"),bg=YELLOW, fg=GREEN)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="Day 28\\tomato.png")

canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill=GREEN,font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset",highlightthickness=0)
reset_button.grid(column=2,row=2)

check_marks = Label(text="x", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1,row=3)



window.mainloop()