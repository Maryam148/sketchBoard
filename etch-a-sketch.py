import turtle as t
tim = t.Turtle()
s = t.Screen()
s.listen()
def move_frwrd():
    tim.forward(10)

def move_bkwrd():
    tim.backward(10)

def turn_right():
    tim.setheading(tim.heading() - 10)

def turn_left():
    tim.setheading(tim.heading() + 10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

s.onkey(move_frwrd,"w")
s.onkey(move_bkwrd,"s")
s.onkey(turn_left,"a")
s.onkey(turn_right,"d")
s.onkey(clear,"c")

s.exitonclick()