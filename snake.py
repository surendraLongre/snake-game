from turtle import Turtle, Screen

class Snake:
    def __init__(self):
        self.score=0
        self.play=True
        self.arr=[Turtle()]
        self.arr[0].color("white")
        self.arr[0].shape("square")
        self.arr[0].penup()

    def add_segment(self):
        self.arr.append(Turtle())
        self.arr[len(self.arr)-1].color("white")
        self.arr[len(self.arr)-1].shape("square")
        self.arr[len(self.arr)-1].penup()
        self.arr[len(self.arr)-1].goto(self.arr[len(self.arr)-2].xcor()-20,self.arr[len(self.arr)-1].ycor())

    def move_snake(self,i):
        self.arr[i].goto(self.arr[i-1].xcor(),self.arr[i-1].ycor())

    def turn_left(self):
        if int(self.arr[0].heading())==90 or int(self.arr[0].heading())==270: 
            self.arr[0].setheading(180)


    def turn_right(self):
        if int(self.arr[0].heading())==90 or int(self.arr[0].heading())==270: 
            self.arr[0].setheading(0)

    def turn_up(self):
        if int(self.arr[0].heading())==0 or int(self.arr[0].heading())==180: 
            self.arr[0].setheading(90)

    def turn_down(self):
        if int(self.arr[0].heading())==0 or int(self.arr[0].heading())==180: 
            self.arr[0].setheading(270)   
