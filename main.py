# import colorgram
#
# colors = colorgram.extract('img.jpg', 27)
# rgb_colors = []
# for color in colors :
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
from turtle import Turtle, Screen
import random

fas = Turtle()
screen =  Screen()
screen.colormode(255)
colors = [(226, 231, 236), (58, 106, 148), (225, 200, 109), (134, 84, 58), (223, 139, 64), (196, 145, 171),
          (224, 234, 230), (234, 226, 203), (142, 179, 204), (139, 81, 105), (210, 91, 68), (188, 79, 118),
          (236, 224, 232), (66, 106, 90), (135, 182, 137), (132, 134, 74), (64, 156, 90), (48, 156, 193),
          (183, 192, 201), (7, 49, 90), (215, 176, 190), (20, 67, 119), (174, 203, 181), (142, 29, 41),
          (225, 175, 168), (113, 124, 149), (65, 52, 38)]
fas.penup()
fas.hideturtle()
# move the turtle down to the south west of the screen
fas.sety(-275)
fas.setx(-320)
current_position = fas.pos()
# for the to determine Y (vertical value)
y_pos = current_position[1]
fas.speed("fastest")
for _ in range (109):
    fas.color(random.choice(colors))
    # to ensure that turtle is only drawing in the screen boundaries untill it reach to the east
    if (fas.xcor() > -350 and fas.xcor() < 350) and (fas.ycor() > -300 and fas.ycor() < 300):
        fas.dot(20)
        fas.fd(70)

    else:
        # changing the turtle position to go up to the above line (vertically)
        y_pos += 60
        fas.goto(current_position[0] ,  y_pos )

screen.exitonclick()
screen.mainloop()