""" Tiro Parabólico """

""" Import functions """
from random import randrange
from turtle import *
from freegames import vector

"""
Equipo 2:
Francisco Vázquez, A00827546
Nicolás Herrera, A01114972
Ana Paula López, A01378255

"""


""" Initial Conditions """
ball = vector(-200, -200)
speed = vector(0, 0)
targets = []

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 200) / 20 # Increase the velocity of the ball from 1/25 to 1/20
        speed.y = (y + 200) / 20

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        """ Move the blue targets """
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        """ Return to home """
        goto(ball.x, ball.y)
        dot(6, 'red')

    update()

def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    " Move the target to the left "
    for target in targets:
        if target.x < -200:
            " When hits the left edge, it goes to the right edge "
            target.x = 200
        else:
            target.x -= 0.7

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed) # Sum the components of the vectors ball with speed

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13: # 13 it is the radius of the target
            targets.append(target)

    """ Create the canvas """
    draw()

    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()