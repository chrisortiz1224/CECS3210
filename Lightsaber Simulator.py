>>> from graphics import *
>>> 
>>> win = GraphWin('Lightsaber Simulator', 1000,200)
>>> win.setBackground("black")
>>> 
>>> lightsaber = Rectangle(Point(50,80), Point(150,110))
>>> lightsaber.setOutline("black")
>>> lightsaber.setFill("gray")
>>> lightsaber.draw(win)
Rectangle(Point(50.0, 80.0), Point(150.0, 110.0))
>>> 
>>> design = Rectangle(Point(60,80), Point(70,90))
>>> design.setFill("black")
>>> design.draw(win)
Rectangle(Point(60.0, 80.0), Point(70.0, 90.0))
>>> 
>>> design2 = design.clone()
>>> design2.move(20,0)
>>> design2.draw(win)
Rectangle(Point(80.0, 80.0), Point(90.0, 90.0))
>>> 
>>> design3 = design2.clone()
>>> design3.move(20,0)
>>> design3.draw(win)
Rectangle(Point(100.0, 80.0), Point(110.0, 90.0))
>>> 
>>> power = design3.clone()
>>> power.setOutline("black")
>>> power.setFill("red")
>>> power.move(20,0)
>>> power.draw(win)
Rectangle(Point(120.0, 80.0), Point(130.0, 90.0))
>>> 
>>> tip = Oval(Point(150,70), Point(160,120))
>>> tip.setOutline("black")
>>> tip.setFill("gold")
>>> tip.draw(win)
Oval(Point(150.0, 70.0), Point(160.0, 120.0))
>>> 
>>> light = Rectangle(Point(160,80), Point(900,110))
>>> light.setOutline("black")
>>> light.setFill("black")
>>> light.draw(win)
Rectangle(Point(160.0, 80.0), Point(900.0, 110.0))
>>> 
>>> blue_saber = Text(Point(100,160), 'Jedi')
>>> blue_saber.setFill("blue")
>>> blue_saber.draw(win)
Text(Point(100.0, 160.0), 'Jedi')
>>> 
>>> button = Rectangle(Point(70,172), Point(150,185))
>>> button.setOutline("blue")
>>> button.setWidth(2)
>>> button.draw(win)
Rectangle(Point(70.0, 172.0), Point(150.0, 185.0))
>>> 
>>> button2 = Rectangle(Point(870,172), Point(930,147))
>>> button2.setOutline("red")
>>> button2.setWidth(2)
>>> button2.draw(win)
Rectangle(Point(870.0, 172.0), Point(930.0, 147.0))
>>> 
>>> red_saber = Text(Point(900, 160), 'Sith')
>>> red_saber.setFill("red")
>>> red_saber.draw(win)
Text(Point(900.0, 160.0), 'Sith')
>>> 
>>> while True:
	p = win.getMouse()
	c = light.getCenter()
	dx = p.getX() - c.getX()
	dy = p.getY() - c.getY()
	button = light.clone()
	button.setFill("blue")
	button.draw(win)
	break

Rectangle(Point(160.0, 80.0), Point(900.0, 110.0))
>>> 
>>> while True:
	p = win.getMouse()
	c = light.getCenter()
	dx = p.getX() - c.getX()
	dy = p.getY() - c.getY()
	button2 = button.clone()
	button2.setFill("red")
	button2.draw(win)
	break

Rectangle(Point(160.0, 80.0), Point(900.0, 110.0))
>>> win.getMouse()
Point(359.0, 140.0)
win.close()
>>> win.close()
>>> 
