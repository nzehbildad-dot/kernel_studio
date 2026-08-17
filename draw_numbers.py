import turtle

def draw_numbers():
    screen = turtle.Screen()
    screen.title("Numbers 1 to 10")
    screen.bgcolor("black")
    screen.setup(width=900, height=300)

    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()
    writer.speed(0)

    drawer = turtle.Turtle()
    drawer.hideturtle()
    drawer.penup()
    drawer.speed(0)
    drawer.pensize(3)

    colors = ["white","red","orange","yellow","green","cyan","blue","magenta","pink","lightgreen"]

    start_x = -350
    y = 0
    spacing = 80

    for i in range(1, 11):
        x = start_x + (i-1) * spacing

        writer.goto(x, y+10)
        writer.color(colors[(i-1) % len(colors)])
        writer.write(str(i), align="center", font=("Arial", 36, "bold"))

        drawer.goto(x, y-40)
        drawer.color(colors[(i-1) % len(colors)])
        drawer.pendown()
        drawer.circle(50)
        drawer.penup()

    screen.mainloop()


if __name__ == "__main__":
    draw_numbers()
