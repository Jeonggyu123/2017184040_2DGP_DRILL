Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import turtle

turtle.shape('turtle')
turtle.stamp()
5
def W_move()
SyntaxError: expected ':'
def W_move():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def A_move():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

    
def S_move():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def D_move():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()

turtle.onkey(restart, 'Escape')
turtle.onkey(W_move, 'w')
turtle.onkey(S_move, 's')
turtle.onkey(a_move, 'a')
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    turtle.onkey(a_move, 'a')
NameError: name 'a_move' is not defined. Did you mean: 'A_move'?
turtle.onkey(A_move, 'a')
turtle.onkey(D_move, 'd')
tutle.listen()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    tutle.listen()
NameError: name 'tutle' is not defined. Did you mean: 'turtle'?
turtle.listen()
