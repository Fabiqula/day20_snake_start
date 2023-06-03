from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")

segment_list = []

def creating_snake():
    x_position = [0, -20, -40]
    for segment_index in range(3):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.pu()
        new_segment.goto(x=x_position[segment_index] , y=0)
        segment_list.append(segment_index)


creating_snake()





















screen.exitonclick()