import display
from math import sin,cos

p = "⬜"
pi = 3.1415926535

#draw pixel
def pixel(x,y):
    display.screen[y][x] = p

#draw rectangle
def rect(x,y,width,height):
    for i in range(width):
        for j in range(height):
            pixel(x+i,int(y+j*0.6))

#draw line
def line(x1,y1,x2,y2):
    #x1==x2
    if x1 == x2 and y1 < y2:
        for i in range(y2-y1):
            pixel(int(x1),int(y1+i))
    
    elif x1 == x2 and y1 > y2:
        for i in range(y1-y2):
            pixel(int(x1),int(y1-i))

    #y1==y2
    if y1 == y2 and x1 < x2:
        for i in range(x2-x1):
            pixel(int(x1+i),int(y1))

    elif y1 == y2 and x1 > x2:
        for i in range(x1-x2):
            pixel(int(x1-i),int(y1))
    
    #check alignment
    if x1 < x2 and y1 < y2:
        a = (y2-y1)/(x2-x1)
        for i in range(x2-x1):
            pixel(int(x1+i),int(y1+i*a))

    elif x1 < x2 and y1 > y2:
        a = (y1-y2)/(x2-x1)
        for i in range(x2-x1):
            pixel(int(x1+i),int(y1-i*a))

    elif x1 > x2 and y1 < y2:
        a = (y2-y1)/(x1-x2)
        for i in range(x1-x2):
            pixel(int(x1-i),int(y1+i*a))

    elif x1 > x2 and y1 > y2:
        a = (y1-y2)/(x1-x2)
        for i in range(x1-x2):
            pixel(int(x1-i),int(y1-i*a))

#draw circle
def circle(x,y,radius):
    for i in range(360):
        pixel(
            int(x+cos(i*pi/180)*radius),
            int(y+sin(i*pi/180)*radius*0.6)
        )
