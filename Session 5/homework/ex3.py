from turtle import *
def draw_square(lengths,colors):
    color(colors)
    for i in range(4):
        forward(lengths)
        left(90)
    mainloop()        
draw_square(90,'blue')