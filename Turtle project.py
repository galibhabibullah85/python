from turtle import*

x=Turtle()
angle=0

def tur():
	x.speed(0)
	x.right(90)
	x.forward(100)

def antitur():
	x.speed(0)
	x.forward(100)
	x.right(90)

def antiinversetur():
	x.speed(0)
	x.right(-90)
	x.forward(100)

def inversetur():
	x.speed(0)
	x.forward(100)
	x.right(-90)

while True:
	tur()
	tur()
	tur()
	tur()

	antitur()
	antitur()
	antitur()
	antitur()

	inversetur()
	inversetur()
	inversetur()
	inversetur()

	antiinversetur()
	antiinversetur()
	antiinversetur()
	antiinversetur()
	angle-=.5
	x.right(angle)

