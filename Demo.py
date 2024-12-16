import turtle
screen = turtle.Screen()
screen.bgcolor("white")
pen = turtle.Turtle()
pen.speed(40)
colors = ["red", "blue", "green", "orange", "purple"]
for i in range(360):
    pen.color(colors[i % len(colors)])  
    pen.forward(i * 2)  
    pen.right(59)  
pen.hideturtle()
screen.mainloop()

