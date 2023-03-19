from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-250, 270)
        self.score = 0
        self.write(f"Level: {self.score}", False, "left", FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Level: {self.score}", False, "left", FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, "center", FONT)


