from turtle import  Turtle
ALIGNMENT = "left"
FONT = ('courier', 18, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.color("white")
        self.ht()
        self.setpos(-250,270)
        self.get_saved_score()
        self.update_scoreboard()

    def get_saved_score(self):
        with open("data.txt") as file:
            data = file.read()
            self.high_score = int(data)

    def save_score(self):
        with open('data.txt', 'w') as file:
            file.write(str(self.score))

    def eat(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} ; HighScore = {self.high_score}", False, align="left", font=('Arial', 12, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_score()
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.update_scoreboard()