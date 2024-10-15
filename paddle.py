from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.paddle_setup(side)

    def paddle_setup(self, side):
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(350, 0) if side == "right" else self.goto(-350, 0)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
