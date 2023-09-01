# Author: Irene Buck
# Date: 8/25/23
# Day 21- Part 2 of 2: Build a Snake Game


from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# screen set up
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')   # background color
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)

    snake.move()

    # Detect collision with food
    # if the distance between the snake and food(2 turtles) is less than 15 pixels (collision occurred)
    if snake.head.distance(food) < 15:
        scoreboard.update_score()
        snake.extend_snake()
        food.refresh_food()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
