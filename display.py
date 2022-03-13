from turtle import Turtle


class Display(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def display_status(self, paused):
        self.clear()
        self.goto(0, 260)
        status = "Press 'space' to Pause/Continue"
        if paused:
            status = "Game is Paused"

        self.write(f"{status}", align="center", font=("Arial", 14, "italic"))


