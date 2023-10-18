from turtle import Turtle

FONT = ('verdana', 20, 'normal')
X = 0
Y = 0
ADD = 20


class Board():

    def __init__(self):
        self.turtle = Turtle()
        self.turtle.penup()
        self.turtle.hideturtle()
        self.tiles = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, '[]']
        ]
        self.draw_tiles()

    def draw_tiles(self):
        x = 0
        y = 0
        add = 50
        for row in self.tiles:
            for col in row:
                self.turtle.goto(x, y)
                self.turtle.write(f'{col}', align='center', font=FONT)
                x += add
            x = 0
            y -= add
