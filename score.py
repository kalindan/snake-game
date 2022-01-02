from turtle import Turtle as t

FONT = ('Arial', 16, 'normal')

ALIGNMENT = "center"

class Score(t):
      def __init__(self):
          super().__init__()    
          self.actual_score = 0
          self.color("white")
          self.penup()
          self.hideturtle()
          self.setpos((0,270))
          self.highscore = 0
          self.load_highscore()
          self.write_score()

      def write_score(self):
          self.clear()
          self.write(f"Game score: {self.actual_score} : High score: {self.highscore} ", False, align=ALIGNMENT,font=FONT)

      def add_point(self):
          self.actual_score += 1
          self.clear()
          self.write(f"Game score: {self.actual_score} : High score: {self.highscore} ", False, align="center",font=('Arial', 16, 'normal'))
     
      def game_over(self):
          self.clear()
          self.write(f"Game over, your final score is {self.actual_score} ", False, align="center",font=('Arial', 16, 'normal'))

      def reset_score(self):
          if self.actual_score > self.highscore:
             self.highscore = self.actual_score
             self.write_highscore()
          self.actual_score = 0

      def load_highscore(self):
          with open("highscore.txt") as file:
             self.highscore = int(file.read())
    
      def write_highscore(self):
          with open("highscore.txt", "w") as file:
             file.write(str(self.highscore))
    