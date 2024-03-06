from tkinter import *

#----- PASSWORD GENERATOR -----
def generate_password():
    return None

#----- SAVE PASSWORD -----
def save_password():
    return None

#----- UI SETUP -----
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

#----- LOGO -----
canvas = Canvas(height=200,width=200)
logo_img = PhotoImage(file="Day 29\logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0, column=1)

#----- LABELS -----
website = Label(text="Website")
website.grid(row=1, column=0)

username = Label(text="Email/Username")
username.grid(row=2, column=0)

password = Label(text="Password")
password.grid(row=3, column=0)

#----- INPUTS -----
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)

username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2)

password_input = Entry()
password_input.grid(row=3, column=1)

#----- BUTTONS -----
gen_pass = Button(text="Generate Password", command=generate_password)
gen_pass.grid(row=3,column=2)

save_pass = Button(text="Save Password", width=36, command=save_password)
save_pass.grid(row=4,column=1,columnspan=2)

window.mainloop()