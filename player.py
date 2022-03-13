from turtle import Turtle
import random

INITIAL_POSITION = (0, -280)
COLORS = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red', 'tomato', 'purple', 'deep pink', 'navy',
          'steel blue', 'aquamarine', 'medium aquamarine', 'orange red', 'pink', 'dark gray']


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.color("red")
        self.goto(INITIAL_POSITION)

    def left_turn(self):
        x = self.xcor() - 10
        self.goto(x, self.ycor())

    def right_turn(self):
        x = self.xcor() + 10
        self.goto(x, self.ycor())

    def up(self):
        self.forward(10)

    def down(self):
        self.backward(10)

    def return_to_start(self):
        self.change_color()
        self.goto(INITIAL_POSITION)

    def change_color(self):
        self.color(random.choice(COLORS))