import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
file_data = pandas.read_csv("50_states.csv")
all_states = file_data.state.to_list()
guessed_state = []
states_missed = []

while len(guessed_state) < 50:
    user_input = screen.textinput(title=f"{len(guessed_state)}/50 State Correct", prompt="What's another state name?").title()
    if user_input == "Exit":
        states_missed = [state for state in all_states if state not in guessed_state]
        new_data = pandas.DataFrame(states_missed)
        new_data.to_csv("states_to_be_learned.csv")
        break
    if user_input in all_states:
        guessed_state.append(user_input)
        state_data = file_data[file_data.state == user_input]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())

