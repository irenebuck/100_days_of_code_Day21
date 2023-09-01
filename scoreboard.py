from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.highest_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(f'Score: {self.score}', align="center", font=("Arial", 12, "bold"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score} Highest Score: {self.highest_score}', align="center", font=("Arial", 12, "bold"))

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(f'{self.score}')
        self.score = 0
        self.clear()
        self.write(f'Score: {self.score} Highest Score: {self.highest_score}', align="center",
                   font=("Arial", 12, "bold"))
