from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            square = Turtle("square")
            square.penup()
            square.color("white")
            square.goto(position)
            #and then we have a list with 3 elements, all together make up a snake:
            self.segments.append(square)

    def move(self, distance):
        for square_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[square_num - 1].xcor()
            new_y = self.segments[square_num - 1].ycor()
            self.segments[square_num].goto(new_x, new_y)
        self.head.forward(distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def level_up(self):
        #position for the new element:
        pos_new_x = self.segments[len(self.segments) - 1].xcor()
        pos_new_y = self.segments[len(self.segments) - 1].ycor()
        new_square = Turtle("square")
        new_square.penup()
        new_square.color("white")
        new_square.goto(pos_new_x,pos_new_y)
        self.segments.append(new_square)
        
    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]