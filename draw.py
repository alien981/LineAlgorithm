from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    pass

def drawOct1(x0, y0, x1, y1, screen, color):
	x = x0
	y = y0
	A = x0-x1
	B = y0-y1
	C = y0*(x0-x1) - x0*(y0-y1)
	d = 2*A + B
	
	while x<250:
		plot(x,y)
		if d>0:
			y+=1
			d +=B
		x+=1
		d += 2 * A
	
	
def drawOct2(x0, y0, x1, y1, screen, color):
	x = x0
	y = y0
	A = x0-x1
	B = y0-y1
	C = y0*(x0-x1) - x0*(y0-y1)
	d = A + 2*B
	
	while y<250:
		plot(x,y)
		if d<0:
			x+=1
			d += 2*A
		y+=1
		d += 2*B
		
def drawOct3(x0, y0, x1, y1, screen, color):
	x = x0
	y = y0
	A = x0-x1
	B = y0-y1
	C = y0*(x0-x1) - x0*(y0-y1)

def drawOct4(x0, y0, x1, y1, screen, color):
	x = x0
	y = y0
	A = x0-x1
	B = y0-y1
	C = y0*(x0-x1) - x0*(y0-y1)

def drawOct5(x0, y0, x1, y1, screen, color):
	x = x0
	y = y0
	A = x0-x1
	B = y0-y1
	C = y0*(x0-x1) - x0*(y0-y1)

def drawOct6(x0, y0, x1, y1, screen, color):
	x = x0
	y = y0
	A = x0-x1
	B = y0-y1
	C = y0*(x0-x1) - x0*(y0-y1)

def drawOct7(x0, y0, x1, y1, screen, color):
	x = x0
	y = y0
	A = x0-x1
	B = y0-y1
	C = y0*(x0-x1) - x0*(y0-y1)


def drawOct8(x0, y0, x1, y1, screen, color):
	x = x0
	y = y0
	A = x0-x1
	B = y0-y1
	C = y0*(x0-x1) - x0*(y0-y1)
	d = 2*A - B
	
	while x<250:
		plot(x,y)
		if d>0:
			y+=1
			d+=2*B
		x+=1
		d+=2*A
		
		