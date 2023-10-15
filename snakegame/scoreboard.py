from turtle import  Turtle
ALIGNMENT = "left"
FONT = ('courier', 18, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.ht()
        self.setpos(-250,270)
        self.write(f"Score = {self.score}", False, align=ALIGNMENT,  font=FONT)

    def eat(self):
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score}", False, align="left", font=('Arial', 12, 'normal'))

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)