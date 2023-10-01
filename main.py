import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("Lightblue")
drawing_board.title("Pyton Turtle")
turtle_instance = turtle.Turtle()
turtle_instance.forward(600)
turtle_instance.left(90)
turtle_instance.forward(200)
turtle_instance.left(90)
turtle_instance.forward(200)
turtle_instance.left(90)
turtle_instance.forward(200)
turtle_instance3 = turtle.Turtle()
for i in range(4):
    turtle_instance3.forward(200)
    turtle_instance3.left(90)
    turtle_instance3.forward(200)
    turtle_instance3.left(90)
    turtle_instance3.forward(200)
    turtle_instance3.left(90)
    turtle_instance3.forward(200)
    turtle_instance3.forward(50)
turtle_instance3.forward(200)


turtle_instance2 = turtle.Turtle()
turtle_instance2.forward(280)
for i in range(10):
    turtle_instance2.left(45)
    turtle_instance2.forward(50)
    turtle_instance2.left(90)
    turtle_instance2.forward(50)














turtle.done()