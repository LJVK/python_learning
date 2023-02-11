from turtle import Turtle, Screen
import random

is_race_on = False
turtle_colors = ["violet", "indigo", "blue", "green", "orange", "red"]
y_coordinate = [-100, -70, -40, -10, 20, 50]
all_turtles = []
s = Screen()
s.setup(width=500, height=400)
user_bet = s.textinput(title="Make your bet", prompt="Which Turtle will win the race? Enter the color: ")

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_coordinate[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Won!! The {winning_color} turtle is the winner")
            else:
                print(f"You Lost. The {winning_color} turtle is the winner")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


s.exitonclick()
