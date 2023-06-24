from turtle import Turtle

file=open("score.txt", mode="r+")
content=file.read()
print(content)

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.highscore=int(content)
        self.goto(0,560)
        self.write_score()
        self.hideturtle()

    def inc_score(self):
        self.score+=1
        self.clear()
        self.write("score: "+str(self.score)+" , high score: "+str(self.highscore), align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center",  font=("Arial", 24, "normal"))


    def write_score(self):
        self.clear()
        self.write("score: "+str(self.score)+" , high score: "+str(self.highscore), align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore=self.score
            file.seek(0)
            file.write(str(self.highscore))
        self.score=0
        self.write_score()
