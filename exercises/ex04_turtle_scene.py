"""Design a structured program and a scene using Turtle."""

__author__ = "730435533"

from turtle import Turtle, colormode, done
colormode(255)


def dark_square(square: Turtle, x: float, y: float) -> Turtle:
    """Creates a black square, showing that it is night time."""
    black_square = Turtle()
    dark_square = black_square
    black_square.pencolor(0, 0, 0)
    black_square.fillcolor(0, 0, 0)
    black_square.penup()
    black_square.goto(x, y)
    black_square.pendown()
    black_square.speed(100)
    i: int = 0
    black_square.begin_fill()
    while(i < 4):
        black_square.forward(600)
        black_square.left(90)
        i = i + 1
# Creates a black square that I will use for the drawing.
    black_square.end_fill()
    return dark_square


def stars(stars: Turtle, x_coordinate: float, y_coordinate: float) -> Turtle:
    """Creates three starts at the top section inside the black square."""
    turtle_stars = Turtle()
    turtle_stars = stars
    turtle_stars.speed(900)
    i: int = 0
    side_length: int = 20
    turtle_stars.pencolor(255, 255, 255)
    while (i < 30):
        turtle_stars.penup()
        turtle_stars.goto(x_coordinate, y_coordinate)
        turtle_stars.pendown()
        turtle_stars.forward(side_length)
        side_length = side_length * 0.97
        turtle_stars.right(152)
        i = i + 1
# creates a start using a loop which makes it look like a spiral
    return turtle_stars


def pyramids(one_pyramid: Turtle, x: float, y: float) -> Turtle:
    """Creates three pyramids inside the black square, indicating that we are in Giza."""
    turtle_pyramids = Turtle()
    one_pyramid = turtle_pyramids
    turtle_pyramids.pencolor(244, 170, 26)
    turtle_pyramids.fillcolor(244, 170, 26)
    turtle_pyramids.penup()
    turtle_pyramids.goto(x, y)
    turtle_pyramids.pendown()
    i: int = 0
    turtle_pyramids.begin_fill()
    while(i < 3):
        turtle_pyramids.forward(300)
        turtle_pyramids.left(120)
        i = i + 1
    turtle_pyramids.end_fill()
# simple drawing of triangles, because they are triangles I used the degrees 120
    return one_pyramid


def alien(one_alien: Turtle, x: float, y: float) -> Turtle:
    """Draws one simple alient spaceship that abducts something on the ground."""
    alien = Turtle()
    one_alien = alien
    alien.pencolor(97, 255, 118)
    alien.fillcolor(97, 255, 118)
    alien.penup()
    alien.goto(x, y)
    alien.pendown()
    alien.speed(100)
    i: int = 0
    alien.begin_fill()
    while(i < 2):
        alien.forward(100)
        alien.left(90)
        alien.forward(50)
        alien.left(90)
        i = i + 1
# creates body of the spaceship
    alien.end_fill()
    alien.penup()
    y = y + 50
    x = x + 10
    alien.goto(x, y)
    alien.pencolor(114, 217, 128)
    alien.fillcolor(97, 255, 118)
    alien.pendown()
    alien.begin_fill()
    i = 0
    while(i < 2):     
        alien.forward(50)
        alien.left(90)
        alien.forward(30)
        alien.left(90)
        i = i + 1
# creates top of the spaceship
    alien.end_fill()
    alien.penup()
    alien.pencolor(177, 218, 182)
    alien.fillcolor(177, 218, 182)
    y -= 300
    alien.goto(x, y)
    alien.pendown()
    i = 0
    alien.begin_fill()
    while(i < 2):
        alien.forward(30)
        alien.left(90)
        alien.forward(250)
        alien.left(90)
        i += 1
# creation of abduction light
    alien.end_fill()
    side_length: int = 30
    i = 0
    alien.pencolor(0, 0, 0)
    while(i < 90):
        side_length = side_length * 0.97
        alien.forward(side_length)
        alien.left(92)
        i += 1
# at the end there is a spral where people get abducted
    alien.penup()
    dots: int = 0
    y_dots: float = 95
    while dots < 28:
        y_dots -= 8
        alien.goto(-260, y_dots)
        alien.dot(5, "green")
        dots += 1
# dots indicating a person being that was being abducted put back on the ground
    return one_alien


def main() -> None:
    """The entry point of the drawing."""
    black_square: Turtle = Turtle()
    turtle_stars: Turtle = Turtle()
    turtle_pyramids: Turtle = Turtle()
    one_alien: Turtle = Turtle()
    dark_square(black_square, -300, -300)
    counting_stars: int = 0
    x_coordinate: float = 0
    y_coordinate: float = 200
    while counting_stars < 2:
        stars(turtle_stars, x_coordinate, y_coordinate)
        x_coordinate += 100
        y_coordinate += 50
        counting_stars += 1
    counting_stars = 0
    x_coordinate = 0
    y_coordinate = 200
    while counting_stars < 1:
        x_coordinate += -100
        y_coordinate += 50
        stars(turtle_stars, x_coordinate, y_coordinate)
        counting_stars += 1
    counting_stars = 1
    x_coordinate = 0
    y_coordinate = 200
    while counting_stars <= 2:
        x_coordinate += 100
        y_coordinate -= 50
        stars(turtle_stars, x_coordinate, y_coordinate)
        counting_stars += 1
# loops to make start appear in different positions
    pyramids(turtle_pyramids, -290, -300)
    counting_pyramids: int = 0
    x_pyramids: int = -290
    y_pyramids: int = -300
    while counting_pyramids < 2:
        x_pyramids += 150
        pyramids(turtle_pyramids, x_pyramids, y_pyramids)
        counting_pyramids += 1
    alien(one_alien, -290, 100)
    done()


if __name__ == "__main__":
    main()
    done()