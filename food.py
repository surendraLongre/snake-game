from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.goto(random.randint(-560, 560), random.randint(-560, 560))

    def pos(self):
        self.goto(random.randint(-560, 560), random.randint(-560, 560))


