from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        pos_x = self.xcor()
        pos_y = self.ycor()
        self.setposition(pos_x, pos_y + 20)

    def go_down(self):
        pos_x = self.xcor()
        pos_y = self.ycor()
        self.setposition(pos_x, pos_y - 20)
