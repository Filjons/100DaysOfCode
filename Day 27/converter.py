from tkinter import *

# Making a button do something
def button_clicked():
    
    miles = input.get()
    km = float(miles) * 1.609344
    result_label.config(text=km) 

result = 0
# Make a window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(height=30, width=50)
# Config a label
input = Entry()
input.grid(column=2, row=1)
miles_label = Label(text="Miles")
miles_label.grid(column=3, row=1)
eq_label = Label(text="is equal to")
eq_label.grid(column=1, row=2)
result_label = Label(text="0")
result_label.grid(column=2, row=2)
button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=3)
km_label = Label(text="Km")
km_label.grid(column=3, row=2)





#my_label["text"] = "New text"
#my_label.config(text="New text")

# Keep the window alive
window.mainloop()