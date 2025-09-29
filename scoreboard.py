from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.sety(270)
        self.score = 0
        self.update_scoreboard()

    def load_high_score(self):
        with open("data.txt") as data:
            return data.read()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score: {self.load_high_score()}", align=ALIGNMENT, font=FONT)

    def score_count(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > int(self.load_high_score()):
            with open("data.txt", "w") as data:
                data.write(str(self.score))
        self.score = 0
        self.update_scoreboard()

'''
    def game_over(self):
        self.sety(0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
'''