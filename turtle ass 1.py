import turtle
import random

screen = turtle.Screen()
screen.setup(900, 600)
screen.bgcolor("#111318")
screen.title("Emo Desk Bot")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

look_x = 0
look_y = 0
target_x = 0
target_y = 0

blinking = False
blink_amount = 0
mood = "happy"

next_look = 80
next_blink = random.randint(100, 250)
next_mood = random.randint(350, 700)


def draw_face():
    t.penup()
    t.goto(-165, -120)
    t.setheading(0)
    t.pendown()

    t.fillcolor("#D9D9D9")
    t.pencolor("#D9D9D9")
    t.begin_fill()

    radius = 35
    for _ in range(2):
        t.forward(260)
        t.circle(radius, 90)
        t.forward(190)
        t.circle(radius, 90)

    t.end_fill()


def draw_eye(x, y, openness=1.0):
    eye_width = 58
    eye_height = 70 * openness

    if openness < 0.15:
        t.penup()
        t.goto(x - 25, y)
        t.pendown()
        t.pencolor("#080808")
        t.pensize(9)
        t.goto(x + 25, y)
        return

    t.penup()
    t.goto(x, y - eye_height / 2)
    t.setheading(0)
    t.pendown()

    t.fillcolor("#F4F4F4")
    t.pencolor("#F4F4F4")
    t.begin_fill()

    for _ in range(2):
        t.circle(eye_width / 2, 90)
        t.circle(eye_height / 2, 90)

    t.end_fill()

    pupil_x = x + look_x
    pupil_y = y + look_y
    pupil_size = 17

    t.penup()
    t.goto(pupil_x, pupil_y - pupil_size)
    t.pendown()
    t.fillcolor("#050505")
    t.pencolor("#050505")
    t.begin_fill()
    t.circle(pupil_size)
    t.end_fill()

    t.penup()
    t.goto(pupil_x - 6, pupil_y + 7)
    t.pendown()
    t.fillcolor("white")
    t.pencolor("white")
    t.begin_fill()
    t.circle(4)
    t.end_fill()


def draw_eyebrows():
    t.pencolor("#080808")
    t.pensize(7)

    if mood == "curious":
        t.penup()
        t.goto(-105, 120)
        t.pendown()
        t.goto(-45, 130)

        t.penup()
        t.goto(45, 130)
        t.pendown()
        t.goto(105, 120)

    elif mood == "sad":
        t.penup()
        t.goto(-105, 130)
        t.pendown()
        t.goto(-45, 120)

        t.penup()
        t.goto(45, 120)
        t.pendown()
        t.goto(105, 130)


def draw_mouth():
    t.pencolor("#080808")
    t.pensize(10)

    if mood == "happy":
        t.penup()
        t.goto(-65, -70)
        t.setheading(-35)
        t.pendown()
        t.circle(80, 70)

    elif mood == "sad":
        t.penup()
        t.goto(-65, -45)
        t.setheading(35)
        t.pendown()
        t.circle(-80, 70)

    elif mood == "surprised":
        t.penup()
        t.goto(0, -90)
        t.pendown()
        t.fillcolor("#080808")
        t.begin_fill()
        t.circle(25)
        t.end_fill()

    elif mood == "sleepy":
        t.penup()
        t.goto(-35, -75)
        t.pendown()
        t.goto(35, -75)

    elif mood == "curious":
        t.penup()
        t.goto(-45, -75)
        t.setheading(-25)
        t.pendown()
        t.circle(55, 50)

    else:
        t.penup()
        t.goto(-45, -75)
        t.pendown()
        t.goto(45, -75)


def draw_bot():
    t.clear()
    draw_face()

    if blinking:
        openness = max(0.02, 1 - blink_amount)
    else:
        openness = 1

    if mood == "sleepy" and not blinking:
        openness = 0.45

    draw_eye(-75, 65, openness)
    draw_eye(75, 65, openness)
    draw_eyebrows()
    draw_mouth()

    screen.update()


def choose_new_look():
    global target_x, target_y

    directions = [
        (-22, 0), (22, 0), (0, 15), (0, -12),
        (-14, 7), (14, 7), (0, 0), (0, 0), (0, 0)
    ]

    target_x, target_y = random.choice(directions)


def start_blink():
    global blinking, blink_amount

    if not blinking:
        blinking = True
        blink_amount = 0


def update_blink():
    global blinking, blink_amount, next_blink

    if blinking:
        blink_amount += 0.18

        if blink_amount >= 1:
            blinking = False
            blink_amount = 0
            next_blink = random.randint(100, 260)


def choose_new_mood():
    global mood, next_mood

    moods = [
        "happy", "happy", "neutral", "neutral",
        "curious", "sleepy", "surprised", "sad"
    ]

    mood = random.choice(moods)
    next_mood = random.randint(350, 750)


def animate():
    global look_x, look_y
    global target_x, target_y
    global next_look, next_blink, next_mood

    if not blinking:
        next_blink -= 1

        if next_blink <= 0:
            start_blink()

    update_blink()

    next_look -= 1

    if next_look <= 0:
        choose_new_look()
        next_look = random.randint(60, 180)

    look_x += (target_x - look_x) * 0.08
    look_y += (target_y - look_y) * 0.08

    next_mood -= 1

    if next_mood <= 0:
        choose_new_mood()

    draw_bot()
    screen.ontimer(animate, 20)


choose_new_look()
draw_bot()
animate()

screen.mainloop()