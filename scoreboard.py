from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.sc = 0
        self.penup()
        self.goto(0,270)
        self.write(f"score: {self.sc} ",align= "center",font=("arial",24,"normal"))
        self.hideturtle()
    def inc(self):
        self.clear()
        self.sc +=1
        self.write(f"score: {self.sc} ",align= "center",font=("arial",24,"normal"))
    def game_over(self):
        self.goto(0,0)
        self.write(f"game over ",align= "center",font=("arial",24,"normal"))
