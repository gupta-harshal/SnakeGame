import turtle
list=[(0,0),(-20,0),(-40,0)]
Move_distance=20
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
    def create_snake(self):
        for i in list:
            self.add_segment(i)
    def add_segment(self,position):
            snake=turtle.Turtle(shape="square")
            snake.color("white")
            snake.penup()
            snake.goto(position)
            self.segments.append(snake)
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def move(self):
        for i in range(len(self.segments)-1,0, -1):
            new_x=self.segments[i-1].xcor()
            new_y=self.segments[i-1].ycor()
            self.segments[i].goto(new_x,new_y)
        self.segments[0].forward(Move_distance)
    def left(self):
        self.segments[0].setheading(180)
    def right(self):
        self.segments[0].setheading(0)
    def up(self):
        self.segments[0].setheading(90)
    def down(self):
        self.segments[0].setheading(270)