from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        #write to file#
        with open("day24_files /Snake+Project+Code+from+Day+21/data.txt") as the_data: 
            self.high_score = str(the_data.read())
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_it(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("day24_files /Snake+Project+Code+from+Day+21/data.txt","w") as the_data:
                the_data.write(f"{self.high_score}")
            
        self.score = 0 #this is crucial to set score to 0, b/c it will never be greater than the first score
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
