from turtle import Turtle
ALIGMENT = "center"
FONT = ("courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.last_high_score()
        self.penup()
        self.goto(0, 250)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', 'w') as file:
                file.write(str(self.high_score))

        self.score = 0
        self.clear()
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGMENT, font=FONT)

    def update_scoreboard(self):
        self.write(
            f"Score: {self.score} High Score: {self.high_score}", align=ALIGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def last_high_score(self):
        with open('data.txt', 'r') as file:
            score = file.read()
            if score == '0' or score == '':
                return 0
            else:
                return int(score)
