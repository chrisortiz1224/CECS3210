from graphics import *


def window(win):
    back = win.setBackground("black")
    lightsaber = Rectangle(Point(50, 80), Point(150, 110))
    lightsaber.setOutline("black")
    lightsaber.setFill("gray")
    lightsaber.draw(win)
    return back


def designs(win, back):
    design = Rectangle(Point(60, 80), Point(70, 90))
    design.setFill("black")
    design.draw(win)

    design2 = design.clone()
    design2.move(20, 0)
    design2.draw(win)

    design3 = design2.clone()
    design3.move(20, 0)
    design3.draw(win)

    power = design3.clone()
    power.setOutline("black")
    power.setFill("red")
    power.move(20, 0)
    power.draw(win)

    tip = Oval(Point(150, 70), Point(160, 120))
    tip.setOutline("black")
    tip.setFill("gold")
    tip.draw(win)

    light = Rectangle(Point(160, 80), Point(900, 110))
    light.setOutline(back)
    light.setFill(back)
    light.draw(win)

    return light


def colors(win):
    blue_saber = Text(Point(100, 160), 'Jedi')
    blue_saber.setFill("blue")
    blue_saber.draw(win)

    button = Rectangle(Point(70, 172), Point(130, 147))
    button.setOutline("blue")
    button.setWidth(2)
    button.draw(win)

    button2 = Rectangle(Point(870, 172), Point(930, 147))
    button2.setOutline("red")
    button2.setWidth(2)
    button2.draw(win)

    red_saber = Text(Point(900, 160), 'Sith')
    red_saber.setFill("red")
    red_saber.draw(win)


def switch(win, light):
    while True:
        win.getMouse()
        saber = light.clone()
        saber.setFill("blue")
        saber.draw(win)
        break

    while True:
        win.getMouse()
        saber2 = light.clone()
        saber2.setFill("red")
        saber2.draw(win)
        break


def main():
    win = GraphWin('Lightsaber Simulator', 1000, 200)
    back = window(win)
    light = designs(win, back)
    colors(win)
    switch(win, light)

    win.getMouse()
    win.close()


main()
