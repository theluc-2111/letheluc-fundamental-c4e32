from turtle import *
def draw_star(x,y,length):
# x: trục ngang: giá trị âm dịch sang trái, giá trị dương dịch sang phải
# y: trục dọc: giá trị âm dịch xuống dưới, giá trị dương dịch lên trên   
    penup()
    setposition(x,y)
    pendown()
    for i in range(5):
        forward(length)
        right(144)
draw_star(-250,0,150)
mainloop()