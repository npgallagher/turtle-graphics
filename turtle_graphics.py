from turtle import *
setup(1100, 700)
bob = Turtle()
jerry = Turtle()
colormode(255)
wn = Screen()



############Functions################
#Keyboard Events
def w():
    forward(45)

def s():
    back(45)

def a():
    left(45)

def d():
    right(45)
    
#Nested Loop
def nested_loop(b,x,y):
    penup()
    goto(x,y)
    pendown()
    while b < 50:
        c = 2
        while c < 50:
            forward(b)
            right(90)
            b = b + 15
            c = c + 6

#Color Function
def color_demo(x,y):
    penup()
    goto(x,y)
    pendown()
    pensize(10)
    pencolor(255,0,0)
    forward(50)
    left(90)
    pencolor(0,255,0)
    forward(50)
    right(90)
    pencolor(0,0,255)
    forward(50)
    pensize(1)
    
#Multiple Turtle Functions
def bob_function(x,y):
    penup()
    goto(x,y)
    pendown()
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    right(90)
    forward(50)
    right(90)

def jerry_function(x,y):
    penup()
    goto(x,y)
    pendown()
    forward(75)
    right(90)
    forward(75)
    right(90)
    forward(75)
    right(90)
    forward(75)
    right(90)

def turtle_functions(x,y):
    jerry.penup()
    jerry.goto(x,y)
    jerry.pendown()
    bob.penup()
    bob.goto(x,y)
    bob.pendown()
    jerry.forward(50)
    jerry.right(90)
    bob.forward(50)
    bob.left(90)
    jerry.forward(50)
    jerry.right(90)
    bob.forward(50)
    bob.left(90)
    jerry.forward(50)
    jerry.right(90)
    bob.forward(50)
    bob.left(90)
    jerry.forward(50)
    jerry.right(90)
    bob.forward(50)
    bob.left(90)

#While Function 
def while_function(a,x,y):
    penup()
    goto(x,y)
    pendown()
    while a < 100:
        forward(a)
        right(90)
        a = a + 2
#For Loop
def for_function(x,y):
    penup()
    goto(x,y)
    pendown()
    for x in range (64):
        forward(50)
        right(63)
speed(10)

#Base Function
def base_function(x,y,points,line,fill):
    penup()
    goto(x, y)
    pendown()

    turn = 180 - (360 / points)

    color(line, fill)

    begin_fill()
    for i in range(points):
        forward(75)
        left(turn)
    end_fill()



##############Draw###########
base_function(0, 0, 36, "green", "blue")
base_function(-75, 0, 36, "blue", "green")
base_function(75, 0, 36, "blue", "green")
for_function(125,125)
for_function(-125, 125)
while_function(10,-125,-125)
while_function(10,125, -125)
bob_function(200, -75)
bob_function(200, -125)
jerry_function(200, -200)
jerry_function(200, -175)
turtle_functions(-200, -25)
color_demo(0, 200)
nested_loop(10, 0, -200)
wn.onkey(w, "w")
wn.onkey(s, "s")
wn.onkey(a, "a")
wn.onkey(d, "d")
wn.listen()
wn.onclick(goto)
turtle.getscreen()._root.mainloop()
wn.mainloop()
