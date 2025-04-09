import turtle

# Setup
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("white")

# Turtle
t = turtle.Turtle()
t1 = turtle.Turtle()


t.speed(5)
t.color("yellow")
t.width(25)#more
t1.speed(15)
t1.color("blue")
t1.width(10)#less

# Draw the "G"
t.circle(100,360)#yellow
t1.circle(100,360)#blue
t1.penup()
t1.goto(30,100)
t1.pendown()
t1.circle(30,360)
t1.circle(10,360)
t1.penup()
t1.goto(-30,100)
t1.pendown()
t1.circle(30,360)    
t1.circle(10,360)
t1.penup()
t1.goto(-10,45) 

t1.circle(30,-60)
t1.pendown()
t1.circle(30,120)

# Hide the turtle
t.hideturtle()

# Keep window open
screen.mainloop()
