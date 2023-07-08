#import our packages
import turtle
import random
import time

# creating a snake game.




# Create scren
screen = turtle.Screen()
screen.title("SNAKE GAME")
screen.setup(width = 700, height = 700)
screen.tracer(0)
screen.bgcolor("#1d1d1d")

#create Border
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(x=-310, y= 250)
turtle.pendown()
turtle.color("red")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.penup()
turtle.hideturtle()

# score
score = 0;
delay = 0.1


#snake
snake = turtle.Turtle()
snake.speed()
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0,0)
snake.direction = 'stop'

#food
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape('square')
fruit.color("white")
fruit.penup()
fruit.goto(30,30)

old_fruit = []

#scoring
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0,300)
scoring.write("SCORE: ", align='center', font=('Courier', 24,"bold"))

# Snake Movement
def snakeUp():
    if snake.direction != "down":
        snake.direction = "up"

def snakeDown():
    if snake.direction != "up":
        snake.direction = "down"

def snakeLeft():
    if snake.direction != "right":
        snake.direction = "left"

def snakeRight():
    if snake.direction != "left":
        snake.direction = "right"

def move():
    if snake.direction =='up':
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction =='down':
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction =='left':
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction =='right':
        x = snake.xcor()
        snake.setx(x + 20)

# Keyboard  binding
screen.listen()
screen.onkeypress(snakeUp,"Up")
screen.onkeypress(snakeDown,"Down")
screen.onkeypress(snakeLeft,"Left")
screen.onkeypress(snakeRight,"Right")

# Main loop
