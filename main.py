from turtle import Screen

from board import Board

screen = Screen()
screen.setup(500, 500)
screen.tracer(0)

board = Board()

screen.update()

screen.exitonclick()
