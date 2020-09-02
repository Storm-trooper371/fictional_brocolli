#spiral of different shapes experiment with turtle
import turtle
window = turtle.Screen()
window.title("drawing")
window.bgcolor("black")

turtle.speed(-100)

def spiral():
    x = 1
    for i in range(180):
        turtle.color("white")
        for j in range(0, 3):
            turtle.forward(x)
            turtle.left(122)
        x += 5
turtle.shape(spiral())
turtle.done()

# for triangle spiral
'''
for j in range(0,3):
    turtle.forward(x)
    turtle.left(122)'''
# for square spiral
'''
for j in range(4):
    turtle.forward(x)
    turtle.right(92)'''
# for circle spiral
'''
for j in range(2):
    turtle.circle(x)
    turtle.left(20)'''