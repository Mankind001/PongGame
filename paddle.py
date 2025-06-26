from turtle import Turtle
from variables import Variables
variables=Variables()
a=variables.a
g=variables.g

class Paddle(Turtle):
    def __init__(self,x,y,color):
        super().__init__()
        self.x=x
        self.y=y
        self.shape("square")
        self.color(color)
        self.shapesize(1,4)
        self.penup()
        self.speed("fastest")
        self.setpos(self.x,self.y)
        self.right(90)

    def up(self):
        if not( (self.xcor()==a and self.ycor()==g) or (self.xcor()==-a and self.ycor()==g)):
            self.forward(-20)

    def down(self):
        if not((self.xcor()==a and self.ycor()==-g) or (self.xcor()==-a and self.ycor()==-g)):
            self.forward(20)





