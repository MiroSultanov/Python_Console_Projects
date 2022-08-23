from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []

y_position = -100
for turtle_index in range(6):
    t = Turtle("turtle")
    t.penup()
    t.color(colors[turtle_index])
    t.goto(x=-230, y=y_position)
    y_position += 40
    turtles.append(t)

if user_bet:
    is_race_on = Turtle

winning_color = ""
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

if winning_color == user_bet:
    print(f"You won! The {winning_color} won the race")
else:
    print(f"Sorry. The {winning_color} won the race.")