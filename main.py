from turtle import Screen, Turtle
import time

#initialize the constants
arr=[] #snake list
score=0
play=True
arr.append(Turtle())
screen=Screen()
screen.setup(width=1200, height=1200)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

#define functions

def add_segment():
    arr.append(Turtle())
    arr[len(arr)-1].color("white")
    arr[len(arr)-1].shape("square")
    arr[len(arr)-1].penup()

def move_snake(i):
    arr[i].goto(arr[i-1].xcor(),arr[i-1].ycor())

def turn_left():
    if int(arr[0].heading())==90 or int(arr[0].heading())==270: 
        arr[0].setheading(180)


def turn_right():
    if int(arr[0].heading())==90 or int(arr[0].heading())==270: 
        arr[0].setheading(0)

def turn_up():
    if int(arr[0].heading())==0 or int(arr[0].heading())==180: 
        arr[0].setheading(90)

def turn_down():
    if int(arr[0].heading())==0 or int(arr[0].heading())==180: 
        arr[0].setheading(270)

#function definitons end
arr[0].color("white")
arr[0].shape("square")
arr[0].penup()
arr[0].speed("slowest")
add_segment()
arr[1].goto(-20,0)

#add key bindings
screen.listen()
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="w", fun=turn_up)
screen.onkey(key="s", fun=turn_down)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="Up", fun=turn_up)
screen.onkey(key="Down", fun=turn_down)

#start the snake game
while play:
    screen.update()
    time.sleep(0.09)
    #exchange the position with the positions of the head
    for i in range(len(arr)-1,0,-1):
        move_snake(i)

    arr[0].forward(20)


#endof snake game

screen.exitonclick()
