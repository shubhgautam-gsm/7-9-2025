import turtle

window = turtle.Screen()
window.screensize(500, 500)
pen = turtle.Turtle()

# Move to the starting position
pen.speed(1)
pen.penup()
pen.goto(-200, 90)#x,y   (-200(backward),90(up))
# pen.goto(-200, -90)#x,y   (-200(backward),-90(down))
pen.pendown()

# Draw a square with gaps between segments
for _ in range(4):
    pen.forward(100)
    pen.penup()  # Lift the pen up before moving to the next corner
    pen.forward(20)  # Move without drawing
    pen.pendown()  # Put the pen down to resume drawing

turtle.done()
