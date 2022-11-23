import turtle
import time
def init_ampel(wn,color):

    wn.title("Riemen Zustand")
    wn.bgcolor("black")

    pen = turtle.Turtle()
    pen.color("yellow")
    pen.width(3)
    pen.hideturtle()
    pen.penup()
    pen.goto(-30, 60)
    pen.pendown()
    pen.fd(60)
    pen.rt(90)
    pen.fd(120)
    pen.rt(90)
    pen.fd(60)
    pen.rt(90)
    pen.fd(120)

    # Red light
    red_light = turtle.Turtle()
    red_light.shape("circle")
    red_light.color("grey")
    red_light.penup()
    red_light.goto(0,40)

    # Yellow light
    yellow_light = turtle.Turtle()
    yellow_light.shape("circle")
    yellow_light.color("grey")
    yellow_light.penup()
    yellow_light.goto(0,0)

    # Green light
    green_light = turtle.Turtle()
    green_light.shape("circle")
    green_light.color("grey")
    yellow_light.penup()
    yellow_light.goto(0,-40)

    if color == "green":
        green_light.color(color)
        yellow_light.color("grey")
        red_light.color("grey")
    elif color == "yellow":
        green_light.color("grey")
        yellow_light.color(color)
        red_light.color("grey")
    else:
        green_light.color("grey")
        yellow_light.color(color)
        red_light.color("red")

