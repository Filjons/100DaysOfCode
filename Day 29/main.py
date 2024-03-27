from tkinter import *
from tkinter import messagebox
import random
#----- Constants -----

DEFAULT_USERNAME = "Angie"
LETTERS = ""
#----- PASSWORD GENERATOR -----
def generate_password():

    password = ""
    for i in range(0,10):

        password += random.choice('0123456789abcdefghijklmn')
    password_input.delete(0,END)
    password_input.insert(END, string=f"{password}")

#----- SAVE PASSWORD -----
'''def save_password():
    
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    if website == "" or username == "" or password == "":
       messagebox.askretrycancel(title="Missing Information", message="Please enter all information.") 
    elif messagebox.askokcancel(title="Save Information",message=f"Is this information correct? \nWebsite: {website}\nUsername: {username}\nPassword: {password}"):
        with open("password_file.txt", "a") as pf:
            pf.write(f"{website} | {username} | {password}\n")
    
        website_input.delete(0,END)
        password_input.delete(0,END)'''
def save_password():
    
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    if website == "" or username == "" or password == "":
       messagebox.askretrycancel(title="Missing Information", message="Please enter all information.") 
    elif messagebox.askokcancel(title="Save Information",message=f"Is this information correct? \nWebsite: {website}\nUsername: {username}\nPassword: {password}"):
        with open("password_file.txt", "a") as pf:
            pf.write(f"{website} | {username} | {password}\n")
    
        website_input.delete(0,END)
        password_input.delete(0,END)

#----- UI SETUP -----
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

#----- LOGO -----
canvas = Canvas(height=200,width=200)
logo_img = PhotoImage(file="Day 29\logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0, column=1)

#----- LABELS -----
website = Label(text="Website")
website.grid(row=1, column=0)

username = Label(text="Email/Username")
username.grid(row=2, column=0,)

password = Label(text="Password")
password.grid(row=3, column=0)

#----- INPUTS -----
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

username_input = Entry(width=35)
username_input.insert(END,string=f"{DEFAULT_USERNAME}")
username_input.grid(row=2, column=1, columnspan=2)

password_input = Entry(width=20)
password_input.grid(row=3, column=1)

#----- BUTTONS -----
gen_pass = Button(text="Generate Password", command=generate_password)
gen_pass.grid(row=3,column=2)

save_pass = Button(text="Save Password", width=30, command=save_password)
save_pass.grid(row=4,column=1,columnspan=2)

window.mainloop()