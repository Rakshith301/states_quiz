import turtle
import pandas
# from turtle import Turtle,Screen
screen = turtle.Screen()
screen.title("US_STATE_GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("./50_states.csv")
list_of_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 Guess the state",
                                    prompt="What's another state's  name").title()
    if answer_state == "Exit":
        missed_states = []
        for state in list_of_states:
            if state not in guessed_states:
                missed_states.append(state)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("States_to_learn.csv")

        break
    if answer_state in list_of_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.iloc[0], state_data.y.iloc[0])
        t.write(state_data.state.item())




# def get_mouse_click_coor(x,y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
