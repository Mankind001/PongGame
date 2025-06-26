from turtle import Turtle


class Score(Turtle):
    def __init__(self, x, y, value):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x, y)
        self.score = value
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"{self.score}", align="center", font=("Courier", 24, "bold"))

    def increase(self):
        self.score += 1
        self.write_score()



