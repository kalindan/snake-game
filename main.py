from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

#Test comment added

#Changing directly in gitHub

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake game")
screen.tracer(0)

my_snake = Snake()
my_snake.make_snake()

snake_food = Food()
snake_food.generate_food()

score = Score()

screen.listen()
screen.onkey(my_snake.up, "Up",)
screen.onkey(my_snake.down, "Down",)
screen.onkey(my_snake.left, "Left",)
screen.onkey(my_snake.right,"Right",)

game_is_on = True
while True:

    screen.update()
    time.sleep(0.1)
    my_snake.move_snake()
    if snake_food.is_food_eaten(my_snake.snake_body[0]):
        my_snake.add_segment()
        score.add_point()
    if my_snake.out_of_bonds() or my_snake.check_collision_with_tail():
        score.reset_score()
        score.write_score()
        my_snake.reset_snake()
        my_snake.make_snake()
        








screen.exitonclick()
