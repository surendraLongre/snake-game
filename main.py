from turtle import Turtle, Screen
import time
from snake import Snake

snake=Snake()
snake.add_segment()

#set screen settings
screen=Screen()
screen.setup(width=1200, height=1200)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

#add key bindings
screen.listen()
screen.onkey(key="a", fun=snake.turn_left)
screen.onkey(key="d", fun=snake.turn_right)
screen.onkey(key="w", fun=snake.turn_up)
screen.onkey(key="s", fun=snake.turn_down)
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="Right", fun=snake.turn_right)
screen.onkey(key="Up", fun=snake.turn_up)
screen.onkey(key="Down", fun=snake.turn_down)


#start the snake game
while snake.play:
    screen.update()
    time.sleep(0.09)
    #exchange the position with the positions of the head
    for i in range(len(snake.arr)-1,0,-1):
        snake.move_snake(i)

    snake.arr[0].forward(20)


#endof snake game

screen=Screen()
screen.exitonclick()
