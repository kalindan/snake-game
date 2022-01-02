from turtle import Turtle as t

MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self):
        self.snake_body = []

    def make_snake(self):
        for i in range(3):
            self.snake_body.append(t())
            self.snake_body[i].shape("square")
            self.snake_body[i].penup()
            self.snake_body[i].setpos(-20*i, 0)
            self.snake_body[i].color("white")
            self.snake_body[i].speed(1)

    def move_snake(self):
        for i in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[i].setpos(self.snake_body[i-1].pos())
        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if not self.snake_body[0].heading() == DOWN:
            self.snake_body[0].setheading(UP)

    def down(self):
        if not self.snake_body[0].heading() == UP:
            self.snake_body[0].setheading(DOWN)
    def left(self):
        if not self.snake_body[0].heading() == RIGHT:
            self.snake_body[0].setheading(LEFT)

    def right(self):
        if not self.snake_body[0].heading() == LEFT:
            self.snake_body[0].setheading(RIGHT)

    def add_segment(self):
        new_segment = t()
        new_segment.shape("square")
        new_segment.penup()
        new_segment.setpos(self.snake_body[len(self.snake_body)-1].pos())
        new_segment.color("white")
        new_segment.speed(1)
        self.snake_body.append(new_segment)

    def out_of_bonds(self):
        return self.snake_body[0].xcor() > 280 or self.snake_body[0].xcor() < -280 or self.snake_body[0].ycor() > 280 or self.snake_body[0].ycor() < -280

    def check_collision_with_tail(self):
        for snake_part in self.snake_body[1:]:
            if self.snake_body[0].distance(snake_part.pos())<5:
                return True
        return False

    def reset_snake(self):
        for segment in self.snake_body:
            segment.reset()
        self.snake_body = []

