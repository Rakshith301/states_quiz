import turtle
import pandas

screen = turtle.Screen()
screen.title("India_state_game")
image = "india-political-map-in-a4-size.gif"
screen.setup(width=800, height=850)
screen.addshape(image)
data = pandas.read_csv("./28_states.csv")
all_states = data.state.to_list()
turtle.shape(image)
guessed_states = []
while len(guessed_states) < 28:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/28 guess the state",
                                    prompt="what's the another state").title()
    if answer_state == "Exit":
        missed_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.iloc[0], state_data.y.iloc[0])
        t.write(state_data.state.item())


#
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

# screen.exitonclick()
