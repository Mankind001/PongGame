from turtle import Turtle
from score import Score
from variables import Variables
variables=Variables()

a=variables.h
b=variables.i

r_score = Score(-a,b, 0)
l_score = Score(a,b, 0)
class Ball(Turtle):
    def __init__(self):
        super().__init__()

        #cange the speed here
        self.speed=3

        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.x = self.speed
        self.y = self.speed


    def move(self):
        new_x = self.xcor() +self.x
        new_y = self.ycor()+self.y
        self.goto(new_x,new_y)
        # self.bounce()

    def bounce(self):
        self.y*=-1

    def lbounceback(self):
        self.x*=-1
        l_score.increase()

    def rbounceback(self):
        self.x*=-1
        r_score.increase()









