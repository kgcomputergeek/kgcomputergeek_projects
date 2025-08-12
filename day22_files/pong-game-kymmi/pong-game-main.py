from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time 



screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("My Pong Game")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up") #up control for the right (aka computer's paddle)
screen.onkey(r_paddle.go_down, "Down") # control for the right (aka computer's paddle)
screen.onkey(l_paddle.go_up, "w") #up control for the right (aka computer's paddle)
screen.onkey(l_paddle.go_down, "s") 


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor()> 270 or ball.ycor() < -270:
        #bouncing needed
        ball.bounce_y()
    
    #collision detection with r_paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()-320:
        #bouncing needed
        ball.bounce_x()

    #r paddle miss detection
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.left_point()

    #l paddle miss detection
    if ball.xcor()< -380:
        ball.reset_position()
        scoreboard.right_point()


    #collision detection with l_paddle



screen.exitonclick()