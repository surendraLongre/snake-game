from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


snake=Snake()
food=Food()
score=ScoreBoard()

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
    #detech colision with food
    if snake.arr[0].distance(food)<20:
        snake.add_segment()
        food.pos()
        score.inc_score()

    #detech collision with the wall
    if abs(int(snake.arr[0].xcor()))>580 or abs(int(snake.arr[0].ycor()))>580:
        print("collided with the wall")
        snake.play=False
        score.game_over()

    #detech collision with the tail

    for segments in snake.arr:
        if segments==snake.arr[0]:
            pass
        elif segments.distance(snake.arr[0])<10:
            snake.play=False
            score.game_over()
            print("collided with its own tail")

#endof snake game

print("done")
screen=Screen()
screen.exitonclick()
