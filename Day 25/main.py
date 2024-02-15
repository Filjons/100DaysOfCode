#import csv
#from numpy import imag
import stat
import pandas as pd
import turtle


'''with open("Day 25\\weather_data.csv") as data_file:
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
#state_list = list(data_file["state"])
state_list = data_file.state.to_list()
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)


answered_states = []
while len(answered_states) < 50:
    answer_state = turtle.textinput(title=f"Guess the State, {len(answered_states)}/50 correct.", prompt="What's another states name?").title()

    if answer_state in state_list:
        answered_states.append(answer_state)
        # Extract the x and y coordinates from the answered state
        state = data_file[data_file.state == answer_state]
        #coordinates = (state["x"].values[0], state["y"].values[0])
        coordinates = (state.x.item(), state.y.item())
        state_writer = turtle.Turtle()
        state_writer.hideturtle()
        state_writer.penup()
        state_writer.goto(coordinates)
        state_writer.write(state.state.item())

    else:
        if answer_state == "Exit":
            break
        else:
            print("That's not a state!")
    #print(.str.match(answer_state))
    #s_count = csv_file.(str(answer_state).title())
remaining_states = [s for s in state_list if s not in answered_states]
'''
for s in state_list:
    if s not in answered_states:
        remaining_states.append(s)
 '''   
pd.DataFrame(remaining_states).to_csv("Day 25\\missing_states")
    
