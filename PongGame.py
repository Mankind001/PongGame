from turtle import Turtle,Screen
from paddle import Paddle
from Ball import Ball
from tkinter import  messagebox
from variables import Variables


variables=Variables()
e=variables.e
f=variables.f
a=variables.a
b=variables.b
c=variables.c
d=variables.d
current_width=variables.current_width
current_height=variables.current_height



screen=Screen()
screen.tracer(0)
screen.setup(current_width,current_height)

screen.bgcolor("black")
screen.title("Pong")

def create_wall():
    line = Turtle()
    line.speed("fastest")
    line.color("white")
    line.pensize(20)

    # Drawing border
    corners = [(e, f), (e, -f), (-e, -f), (-e, f), (e, f)]
    line.penup()
    for x, y in corners:
        line.goto(x, y)
        line.pendown()

    # Drawing net
    line.penup()
    line.goto(0, f)
    line.setheading(270)
    line.pensize(5)
    while line.ycor() > -f:
        line.pendown()
        line.forward(20)
        line.penup()
        line.forward(20)
create_wall()

r_paddle=Paddle(x=a,y=0,color="red")
l_paddle=Paddle(x=-a,y=0,color="blue")
ball=Ball()


screen.listen()
screen.onkey(fun=r_paddle.up,key="Up")
screen.onkey(fun=r_paddle.down,key="Down")
screen.onkey(fun=l_paddle.up,key="W")
screen.onkey(fun=l_paddle.up,key='w')
screen.onkey(fun=l_paddle.down,key="S")
screen.onkey(fun=l_paddle.down,key="s")


game_is_on=True
can_bounce=True
while game_is_on:
    screen.update()
    ball.move()

    if ball.ycor()>b or ball.ycor()<-(b):
        ball.bounce()

    if ball.xcor()>=c and ball.distance(r_paddle) < 50 and can_bounce:
        ball.lbounceback()
        can_bounce=False
    elif ball.xcor() <= -c and ball.distance(l_paddle) < 50 and can_bounce:
        ball.rbounceback()
        can_bounce=False

    if -d< ball.xcor()<d:
        can_bounce = True

    if ball.xcor() >=a or ball.xcor() <= -a:
        # pass
        if ball.xcor() >= a:
            messagebox.showinfo("GAME OVER","BLUE WINS")
        elif ball.xcor() <= -a:
            messagebox.showinfo("GAME OVER", "RED WINS")
        screen.bye()
        game_is_on=False




screen.exitonclick()