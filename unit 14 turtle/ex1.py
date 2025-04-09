import turtle

window = turtle.Screen()
window.setup(height=500,width=500)
pen = turtle.Turtle()

# Draw vertical line
pen.left(90)  # Turn left to face upward
pen.forward(400)  # Move upward

# Draw horizontal line
pen.right(120)  # Turn right to face right
pen.forward(200)  # Move to the right

pen.right(90)  # Turn left to face upward
pen.forward(400) 
turtle.done() # not exit the box