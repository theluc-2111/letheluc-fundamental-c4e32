from turtle import *
def draw_square(lengths,colors):
    color(colors)
    for i in range(4):
        forward(lengths)
        left(90)       
for i in range(30):
    draw_square(i*5,'red')
    left(17)
    penup()
    forward(i*2)
    pendown()
mainloop()      