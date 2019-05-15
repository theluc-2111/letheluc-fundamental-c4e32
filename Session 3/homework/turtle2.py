from turtle import *
colors = ["red","blue","brown","yellow","grey"]
speed(1)   
for i in range(len(colors)):
    color(colors[i])
    fillcolor(colors[i])
    begin_fill()
    for j in range(2):
        forward(60)
        left(90)
        forward(90)
        left(90)
    end_fill()
    forward(60)    
mainloop()