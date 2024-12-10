from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('./data.txt', mode='r') as highscore:
            value = highscore.read()
            self.highscore = int(value)
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.color('white')
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.display_score()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open('./data.txt', mode='w') as data:
                data.write(str(self.highscore))

        self.score = 0
        self.display_score()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)