from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 10, "normal")
GAME_OVER_FONT = ("Arial", 20, "normal")


class Pointer(Turtle):

    def __init__(self):
        super().__init__()
        self.n_states = 0
        self.ht()
        self.penup()

    def write_state(self, state, coordinates: tuple[int, int]):
        self.n_states += 1
        self.goto(coordinates)
        self.write(arg=state, align=ALIGN, font=FONT)

    def guessed_all(self):
        self.goto(0, 260)
        self.write(arg="You guessed all states!", align=ALIGN, font=GAME_OVER_FONT)
