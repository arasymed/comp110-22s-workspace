from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
bob: Turtle = Turtle()

# leo.forward(90)
# leo.left(90)
# leo.forward(90)
# leo.left(90)
# leo.forward(90)
# leo.left(90)
# leo.forward(90)
# done()

leo.color(255, 214, 254)
leo.penup()
leo.goto(-250, -250)
leo.pendown()
leo.begin_fill()
leo.speed(50)
leo.hideturtle()
i: int = 0
while(i < 3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
leo.end_fill()

bob.pencolor(136, 120, 210)
bob.fillcolor(189, 179, 231)
bob.penup()
bob.goto(-250, -250)
bob.pendown()
bob.speed(100)
side_length: int = 300
i = 0
while(i < 3):
    bob.forward(side_length)
    bob.left(120)
    i = i + 1

while(i < 150):
    side_length = side_length * 0.97
    bob.forward(side_length)
    bob.left(122)
    i = i + 1
    
done()
