from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        segment = Turtle('square')
        segment.color('white')
        segment.penup()
        segment.goto(position)
        self.snake_segments.append(segment)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())

    def reset(self):
        for seg in self.snake_segments:
            seg.goto(1000, 1000)
        self.snake_segments.clear()
        self.create_snake()
        self.head = self.snake_segments[0]

    def move(self):
        for segment in range(len(self.snake_segments) - 1, 0, -1):
            new_xcor = self.snake_segments[segment - 1].xcor()
            new_ycor = self.snake_segments[segment - 1].ycor()
            self.snake_segments[segment].goto(new_xcor, new_ycor)
        self.snake_segments[0].forward(MOVE_DISTANCE)

    def turn_right(self):
        current_heading = self.head.heading()
        if current_heading != LEFT:
            self.head.setheading(0)

    def turn_up(self):
        current_heading = self.head.heading()
        if current_heading != DOWN:
            self.head.setheading(90)

    def turn_left(self):
        current_heading = self.head.heading()
        if current_heading != RIGHT:
            self.head.setheading(180)

    def turn_down(self):
        current_heading = self.head.heading()
        if current_heading != UP:
            self.head.setheading(270)
