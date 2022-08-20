from turtle import Screen, Turtle

from pong_game.ball import Ball
from pong_game.paddle import Paddle
import time

from score_board import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
score_board = ScoreBoard()

ball = Ball()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect collision with a wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < - 320:
        ball.bounce_x()

    #detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.l_point()

    # detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_point()

screen.exitonclick()