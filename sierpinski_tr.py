import turtle


def draw_triangle(some_turtle, side_size):
	angle = 60
	for i in range(0, 3):
		some_turtle.forward(side_size)
		some_turtle.left(180 - angle)

def sierpinski_triangle(some_turtle, side_size, depth):
	if depth == 0:
		return
	some_turtle.forward(side_size / 2)
	some_turtle.left(60)
	draw_triangle(some_turtle, side_size / 2)
	some_turtle.left(-60)
	sierpinski_triangle(some_turtle, side_size / 2, depth - 1)
	some_turtle.left(120)
	some_turtle.forward(side_size / 2)
	some_turtle.left(-120)
	sierpinski_triangle(some_turtle, side_size / 2, depth - 1)
	some_turtle.left(-120)
	some_turtle.forward(side_size / 2)
	some_turtle.left(120)
	sierpinski_triangle(some_turtle, side_size / 2, depth - 1)



def sierpinski_stack(some_turtle, side_size, depth):
	draw_triangle(some_turtle, side_size / 2)
	list_stack = []
	list_stack.append((some_turtle, side_size, depth))
	while len(list_stack) != 0:
		some_turtle, side_size, depth = list_stack.pop()
		some_turtle.forward(side_size / 2)
		some_turtle.left(60)
		draw_triangle(some_turtle, side_size / 2)
		some_turtle.left(-60)
		list_stack.append((some_turtle, side_size, depth))
        list_stack.append((some_turtle, side_size, depth))
        list_stack.append((some_turtle, side_size, depth))







def main():
	window = turtle.Screen()
	brad = turtle.Turtle()
	brad.speed(1)
	draw_triangle(brad, 300)
	sierpinski_triangle(brad, 300, 2)


main()
