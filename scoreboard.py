from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(f'Score: {self.score}', align="center", font=("Arial", 12, "bold"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}', align="center", font=("Arial", 12, "bold"))

    def game_over(self):
        self.penup()
        self.goto(0, 0)
        self.write(f'GAME OVER', align="center", font=("Arial", 25, "bold"))


