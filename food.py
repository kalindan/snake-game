from turtle import Turtle as t
import random

class Food(t):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("red")

    def generate_food(self):
        self.setpos(random.randrange(-240,240,20), random.randrange(-240,240,20))

    def is_food_eaten(self, snake_head):
        if snake_head.distance(self.pos()) < 10.0:
            self.generate_food()
            return True
