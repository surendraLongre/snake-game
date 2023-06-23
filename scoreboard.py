from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.goto(0,560)
        self.write("score: "+str(self.score), align="center", font=("Arial", 24, "normal"))
        self.hideturtle()

    def inc_score(self):
        self.score+=1
        self.clear()
        self.write("score: "+str(self.score), align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center",  font=("Arial", 24, "normal"))
