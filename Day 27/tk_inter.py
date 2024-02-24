from tkinter import *

# Make a window
window = Tk()
window.title("My window")
window.minsize(width=500, height=300)
# Config a label
my_label = Label(text="I'm a label", font=("Arial", 24, "bold"))
my_label.pack(side="left")

my_label["text"] = "New text"
my_label.config(text="New text")

# Making a button do something
def button_clicked():
    print("I got clicked!")
    print(input.get())

button = Button(text="Click Me", command=button_clicked)
button.pack()

# Get some input

input = Entry(width=10)
input.pack()

print(input.get())

# Keep the window alive
window.mainloop()