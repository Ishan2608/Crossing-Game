from turtle import Turtle

ALIGN = 'center'
FONT = ("Arial", 20, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 0
        with open('high_score_keeper.txt') as data:
            self.highest_level = int(data.read())
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-240, 260)
        self.write(f"Level: {self.level}", align=ALIGN, font=FONT)
        self.goto(-225, 240)
        self.write(f"High Level: {self.highest_level}", align=ALIGN, font=("Arial", 16, "normal"))

    def increase_score(self):
        self.level += 1
        if self.level > self.highest_level:
            with open("high_score_keeper.txt", mode='w') as data:
                self.highest_level = self.level
                data.write(str(self.level))
        self.update_score()

    def show_game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGN, font=("Courier", 60, "normal"))

    def display_status(self, paused):
        self.clear()
        self.goto(0, -260)
        status = ""
        if paused:
            status = "Game is Paused"
        self.write(f"{status}", align=ALIGN, font=("Arial", 18, "normal"))
