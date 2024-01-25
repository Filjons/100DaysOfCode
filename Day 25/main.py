#import csv
#from numpy import imag
import pandas as pd
import turtle


'''with open("Day 25\weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))
        
    print(temperatures)



data = pd.read_csv("Day 25\weather_data.csv")

temp_list = data["temp"].to_list()
sum_temp = 0
for num in temp_list:
    sum_temp += int(num)

avg_temp = sum_temp/len(temp_list)
print(temp_list)
print(avg_temp)

# Pandas functions to get values.
mean = data["temp"].mean()
max = data["temp"].max()
min = data["temp"].min()

#print(mean, max, min)

# Pandas to get rows

#print(data[data.temp == max])

monday = data[data.day == "Monday"]

celsius = monday.temp[0]
fahrenheit = (celsius * 1.8) + 32

print(fahrenheit)

csv_file = pd.read_csv("Day 25\Squirrel_Data.csv")

s_count = csv_file.value_counts("Primary Fur Color")

s_count.to_csv("Day 25\Squirrel_count.csv")'''

# Setup
DATA_FILE = "Day 25\\50_states.csv"
IMAGE = "Day 25\\blank_states_img.gif"

data_file = pd.read_csv(DATA_FILE)

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

answer_state = screen,turtle.textinput(title="Guess the State", prompt="What's another states name?")
s_count = csv_file.(str(answer_state).title())
turtle.mainloop()
