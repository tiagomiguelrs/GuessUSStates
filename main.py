from turtle import Screen, Turtle
from pointer import Pointer
import pandas as pd

GUESSED_ALL = False

screen = Screen()
screen.bgpic("blank_states_img.gif")

states_df = pd.read_csv("50_states.csv")
states_df.set_index("state", inplace=True)

print(states_df)

pointer = Pointer()

while not GUESSED_ALL:

    state = screen.textinput(title=f"{pointer.n_states}/50 guessed.", prompt="Guess another state:").title()
    print(state)

    if state == "Exit":
        GUESSED_ALL = True

    if state in states_df.index:
        coordinates = tuple(states_df.loc[state])
        pointer.write_state(state, coordinates)
        states_df.drop(state, inplace=True)

    if pointer.n_states == 50:
        GUESSED_ALL = True
        pointer.guessed_all()

states_df.reset_index(inplace=True)
states_df.to_csv("states_to_learn.csv", mode="w")

screen.mainloop()