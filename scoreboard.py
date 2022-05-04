from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-270, 270)
        self.update_scoreBoard()

    def update_scoreBoard(self):
        self.clear()
        self.write(f"Level : {self.level}",align="left",font=FONT)


    def increment(self):
        self.update_scoreBoard()
        self.level += 1

    def Game_Over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)



