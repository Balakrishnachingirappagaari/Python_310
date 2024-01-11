import turtle

def draw_star_usinglines():
    screen =turtle.Screen()
    screen.bgcolor("blue")
    screen.title("Drawing lines Practice")

    my_turtle=turtle.Turtle()
    #my_turtle.shape("turtle")
    my_turtle.forward(100)
    for x in range(0,8):
        my_turtle.pencolor("red")
        my_turtle.forward(100)
        my_turtle.backward(100)
        my_turtle.pencolor("black")
        my_turtle.left(45)
    
    my_turtle.hideturtle()
    turtle.done()
    
def draw_circle():
    screen=turtle.Screen()
    screen.bgcolor("blue")
    screen.title("Drawing circle")
    my_turtle=turtle.Turtle()
    my_turtle.pensize(5)
    my_turtle.fillcolor("red")
    my_turtle.begin_fill()
    my_turtle.circle(100)
    turtle.done

draw_circle()
#draw_star_usinglines()