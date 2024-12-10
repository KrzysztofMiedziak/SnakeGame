from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self, snake_segments=None):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        position = (random_x, random_y)
        already_existing_segments_positions = []
        if snake_segments is not None:
            for i in snake_segments:
                seg_position_x = i.xcor()
                seg_position_y = i.ycor()
                existing_position = (seg_position_x, seg_position_y)
                already_existing_segments_positions.append(existing_position)
            if position not in already_existing_segments_positions:
                self.goto(position)

