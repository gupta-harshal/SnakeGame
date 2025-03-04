from turtle import Turtle,Screen
from snake import Snake
from food import Food
import time
from scoreboard import Score
screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)
snake=Snake()
score=Score()
food=Food()
screen.listen()
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect collsion with food
    if snake.segments[0].distance(food)<15:
        food.create_food()
        score.increase_score()
        snake.extend()
    if snake.segments[0].xcor()>290 or snake.segments[0].xcor()<-290 or snake.segments[0].ycor()>290 or snake.segments[0].ycor()<-290:
        game_is_on=False
        score.game_over()
    for seg in snake.segments[1:]:
        if snake.segments[0].distance(seg)<19:
            game_is_on=False
            score.game_over()
 


screen.exitonclick()