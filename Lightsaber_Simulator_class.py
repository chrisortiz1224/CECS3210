from graphics import *


class Lightsaber:

    def __init__(self,win):
        self.win = win

    def window(self,win):
        self.lightsaber = Rectangle(Point(50, 80), Point(150, 110))
        self.lightsaber.setOutline("black")
        self.lightsaber.setFill("gray")
        self.lightsaber.draw(win)

    def designs(self,win):
        self.design = Rectangle(Point(60, 80), Point(70, 90))
        self.design.setFill("black")
        self.design.draw(win)

        self.design2 = self.design.clone()
        self.design2.move(20, 0)
        self.design2.draw(win)

        self.design3 = self.design2.clone()
        self.design3.move(20, 0)
        self.design3.draw(win)

        self.power = self.design3.clone()
        self.power.setOutline("black")
        self.power.setFill("red")
        self.power.move(20, 0)
        self.power.draw(win)

        self.tip = Oval(Point(150, 70), Point(160, 120))
        self.tip.setOutline("black")
        self.tip.setFill("gold")
        self.tip.draw(win)

        self.light = Rectangle(Point(160, 80), Point(900, 110))
        self.light.setOutline("black")
        self.light.setFill("black")
        self.light.draw(win)

        while True:
            win.getMouse()
            self.saber = self.light.clone()
            self.saber.setFill("blue")
            self.saber.draw(win)
            break

        while True:
            win.getMouse()
            self.saber2 = self.light.clone()
            self.saber2.setFill("red")
            self.saber2.draw(win)
            break

    def colors(self,win):
        self.blue_saber = Text(Point(100, 160), 'Jedi')
        self.blue_saber.setFill("blue")
        self.blue_saber.draw(win)

        self.button = Rectangle(Point(70, 172), Point(130, 147))
        self.button.setOutline("blue")
        self.button.setWidth(2)
        self.button.draw(win)

        self.button2 = Rectangle(Point(870, 172), Point(930, 147))
        self.button2.setOutline("red")
        self.button2.setWidth(2)
        self.button2.draw(win)

        self.red_saber = Text(Point(900, 160), 'Sith')
        self.red_saber.setFill("red")
        self.red_saber.draw(win)


def main():
        win = GraphWin('Lightsaber Simulator', 1000, 200)
        win.setBackground("black")
        saber = Lightsaber(win)
        saber.window(win)
        saber.colors(win)
        saber.designs(win)


        win.getMouse()
        win.close()

main()
