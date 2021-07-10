from lark import Lark
import turtle

def interpret(t):
	if t.data == 'move':
		m, a = t.children
		if m == 'f':
			turtle.fd(int(a))
		elif m == 'b':
			turtle.bk(int(a))
		elif m == 'r':
			turtle.rt(int(a))
		elif m == 'l':
			turtle.lt(int(a))
			
	elif t.data == 'control':
		c = t.children[0]
		if c == 'u':
			turtle.penup()
		elif c == 'd':
			turtle.pendown()
		elif c == 'h':
			turtle.hideturtle()
		else:
			turtle.showturtle()
			
	elif t.data == 'color':
		turtle.color(t.children[0])
			
	elif t.data == 'fill':
		turtle.begin_fill()
		interpret(t.children[0])
		turtle.end_fill()
		
	elif t.data == 'repeat':
		for i in range(int(t.children[0])):
			interpret(t.children[1])
			
	elif t.data == 'block':
		for i in t.children:
			interpret(i)
			
					
def run(code):
	parser = Lark(open('grammar.lark').read())
	parsed = parser.parse(code)
	turtle.speed(0)
	for t in parsed.children:
		interpret(t)
