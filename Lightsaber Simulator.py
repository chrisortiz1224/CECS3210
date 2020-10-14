from graphics import *
 
win = GraphWin('Lightsaber Simulator', 1000,200)
win.setBackground("black")
 
lightsaber = Rectangle(Point(50,80), Point(150,110))
lightsaber.setOutline("black")
lightsaber.setFill("gray")
lightsaber.draw(win)

design = Rectangle(Point(60,80), Point(70,90))
design.setFill("black")
design.draw(win)

design2 = design.clone()
design2.move(20,0)
design2.draw(win)

design3 = design2.clone()
design3.move(20,0)
design3.draw(win)

power = design3.clone()
power.setOutline("black")
power.setFill("red")
power.move(20,0)
power.draw(win)

tip = Oval(Point(150,70), Point(160,120))
tip.setOutline("black")
tip.setFill("gold")
tip.draw(win)

light = Rectangle(Point(160,80), Point(900,110))
light.setOutline("black")
light.setFill("black")
light.draw(win)

blue_saber = Text(Point(100,160), 'Jedi')
blue_saber.setFill("blue")
blue_saber.draw(win)

button = Rectangle(Point(70,172), Point(150,185))
button.setOutline("blue")
button.setWidth(2)
button.draw(win)

button2 = Rectangle(Point(870,172), Point(930,147))
button2.setOutline("red")
button2.setWidth(2)
button2.draw(win)

red_saber = Text(Point(900, 160), 'Sith')
red_saber.setFill("red")
red_saber.draw(win)

while True:
	p = win.getMouse()
	c = light.getCenter()
	dx = p.getX() - c.getX()
	dy = p.getY() - c.getY()
	button = light.clone()
	button.setFill("blue")
	button.draw(win)
	break


while True:
	p = win.getMouse()
	c = light.getCenter()
	dx = p.getX() - c.getX()
	dy = p.getY() - c.getY()
	button2 = button.clone()
	button2.setFill("red")
	button2.draw(win)
	break

win.getMouse()
win.close()

